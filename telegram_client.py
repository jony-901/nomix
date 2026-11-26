"""
Telegram Bot Engine using standard Python libraries (urllib, json, ssl, time).
Zero external dependencies required - works out of the box!
"""

import json
import logging
import ssl
import sys
import time
import urllib.parse
import urllib.request
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger("tg_client")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class TelegramBot:
    def __init__(self, token: str):
        self.token = token.strip()
        self.api_url = f"https://api.telegram.org/bot{self.token}/"
        # Create SSL context with fallback for Mac system python cert issues
        self.ssl_ctx = ssl.create_default_context()
        try:
            import certifi
            self.ssl_ctx.load_verify_locations(certifi.where())
        except Exception:
            # Fallback if certifi not found
            self.ssl_ctx.check_hostname = False
            self.ssl_ctx.verify_mode = ssl.CERT_NONE

    def call_api(self, method: str, data: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Call Telegram Bot API method."""
        url = self.api_url + method
        headers = {"Content-Type": "application/json"}
        payload = json.dumps(data or {}).encode("utf-8")

        req = urllib.request.Request(url, data=payload, headers=headers)
        try:
            with urllib.request.urlopen(req, context=self.ssl_ctx, timeout=35) as resp:
                body = resp.read().decode("utf-8")
                res = json.loads(body)
                if not res.get("ok"):
                    logger.error("API error for %s: %s", method, res.get("description"))
                return res
        except urllib.error.HTTPError as e:
            try:
                err_body = e.read().decode("utf-8")
                logger.error("HTTP error %s for %s: %s", e.code, method, err_body)
            except Exception:
                logger.error("HTTP error %s for %s", e.code, method)
            return None
        except Exception as e:
            logger.error("Request failed for %s: %s", method, e)
            return None

    def get_me(self) -> Optional[Dict[str, Any]]:
        return self.call_api("getMe")

    def send_message(
        self,
        chat_id: int,
        text: str,
        parse_mode: str = "HTML",
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        data = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
        }
        if reply_markup:
            data["reply_markup"] = reply_markup
        return self.call_api("sendMessage", data)

    def edit_message_text(
        self,
        chat_id: int,
        message_id: int,
        text: str,
        parse_mode: str = "HTML",
        reply_markup: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": parse_mode,
        }
        if reply_markup:
            data["reply_markup"] = reply_markup
        return self.call_api("editMessageText", data)

    def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: bool = False,
    ) -> Optional[Dict[str, Any]]:
        data: Dict[str, Any] = {"callback_query_id": callback_query_id}
        if text:
            data["text"] = text
            data["show_alert"] = show_alert
        return self.call_api("answerCallbackQuery", data)

    def get_updates(self, offset: Optional[int] = None, timeout: int = 25) -> List[Dict[str, Any]]:
        data: Dict[str, Any] = {"timeout": timeout}
        if offset is not None:
            data["offset"] = offset
        res = self.call_api("getUpdates", data)
        if res and res.get("ok"):
            return res.get("result", [])
        return []

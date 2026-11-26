const express = require('express');
const path = require('path');
const https = require('https');

const app = express();
const PORT = process.env.PORT || 3000;
const BOT_TOKEN = process.env.TELEGRAM_BOT_TOKEN || '9197793802:AAE1YqPe3LuoSvRgqh9dIlq1EDG7oI8WZ-4';
const TELEGRAM_API = `https://api.telegram.org/bot${BOT_TOKEN}`;

// Serve static frontend web app
app.use(express.static(path.join(__dirname)));
app.use(express.json());

// Telegram API Helper
function callTelegram(method, data) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify(data);
    const url = new URL(`${TELEGRAM_API}/${method}`);
    const req = https.request(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(payload)
      }
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(body)); } catch (e) { resolve({ ok: false, error: e }); }
      });
    });
    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

// Country & Pool Data for Telegram Engine
const DATA = require('./data.json');
const COUNTRIES = DATA.countries;
const POOLS = DATA.pools;

const POPULAR_CODES = ["BD", "US", "GB", "IN", "JP", "DE"];
const PAGE_SIZE = 6;

function searchCountries(query) {
  const q = query.trim().toLowerCase();
  if (!q) return [];
  const exact = [], prefix = [], substring = [];
  COUNTRIES.forEach(c => {
    const nameL = c.name.toLowerCase();
    const codeL = c.code.toLowerCase();
    const aliases = (c.aliases || []).map(a => a.toLowerCase());
    if (nameL === q || codeL === q || aliases.includes(q)) exact.push(c);
    else if (nameL.startsWith(q) || codeL.startsWith(q) || aliases.some(a => a.startsWith(q))) prefix.push(c);
    else if (nameL.includes(q) || aliases.some(a => a.includes(q))) substring.push(c);
  });
  return [...exact, ...prefix, ...substring];
}

function getRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function generateNames(poolKey, count = 5, gender = 'all') {
  const pool = POOLS[poolKey] || POOLS['anglo_western'];
  const males = pool.male_first || [];
  const females = pool.female_first || [];
  const lasts = pool.last_names || [];

  const list = [];
  for (let i = 0; i < count; i++) {
    let first = '', icon = '';
    if (gender === 'male') {
      first = getRandom(males); icon = '👨';
    } else if (gender === 'female') {
      first = getRandom(females); icon = '👩';
    } else {
      if (Math.random() < 0.5) { first = getRandom(males); icon = '👨'; }
      else { first = getRandom(females); icon = '👩'; }
    }
    const last = getRandom(lasts);
    list.push(`${icon} ${first} ${last}`);
  }
  return list;
}

function buildCountryKeyboard(page = 1, query = null) {
  let list = [];
  if (query) {
    list = searchCountries(query);
  } else {
    const feat = COUNTRIES.filter(c => POPULAR_CODES.includes(c.code));
    const rest = COUNTRIES.filter(c => !POPULAR_CODES.includes(c.code));
    list = [...feat, ...rest];
  }

  const total = list.length;
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  page = Math.max(1, Math.min(page, totalPages));

  const start = (page - 1) * PAGE_SIZE;
  const items = list.slice(start, start + PAGE_SIZE);

  const keyboard = [];
  let row = [];
  items.forEach(c => {
    row.push({ text: `${c.flag} ${c.name}`, callback_data: `sel:${c.code}` });
    if (row.length === 2) {
      keyboard.push(row);
      row = [];
    }
  });
  if (row.length > 0) keyboard.push(row);

  const navRow = [];
  const prefix = query ? `sq:${query}` : 'page';
  if (page > 1) navRow.push({ text: '⬅️ Prev', callback_data: `${prefix}:${page - 1}` });
  navRow.push({ text: `📄 ${page}/${totalPages}`, callback_data: 'noop' });
  if (page < totalPages) navRow.push({ text: 'Next ➡️', callback_data: `${prefix}:${page + 1}` });
  keyboard.push(navRow);

  const actionRow = [{ text: '🔍 Search Country', callback_data: 'search_prompt' }];
  if (query) actionRow.push({ text: '🏠 Home (All)', callback_data: 'home' });
  keyboard.push(actionRow);

  return { inline_keyboard: keyboard };
}

function renderCountryScreen(countryCode, gender = 'all', count = 5) {
  const country = COUNTRIES.find(c => c.code === countryCode);
  if (!country) return { text: '❌ দেশ খুঁজে পাওয়া যায়নি!', markup: buildCountryKeyboard() };

  const names = generateNames(country.pool, count, gender);
  const namesText = names.map(n => `• <b>${n}</b>`).join('\n');
  const genderLabel = gender === 'all' ? 'উভয় (Both)' : (gender === 'male' ? 'পুরুষ (Male)' : 'মহিলা (Female)');

  const text = `${country.flag} <b>${country.name} — নাম জেনারেটর</b>\n━━━━━━━━━━━━━━━━━━━━\n🎯 <b>ফিল্টার:</b> ${genderLabel} | সংখ্যা: ${count} টি\n\n${namesText}\n\n<i>💡 নিচের বাটনে চাপ দিয়ে আনলিমিটেড নতুন নাম পান:</i>`;

  const markup = {
    inline_keyboard: [
      [
        { text: '🔄 Generate Again (5)', callback_data: `gen:${countryCode}:${gender}:5` },
        { text: '⚡ Generate 10', callback_data: `gen:${countryCode}:${gender}:10` }
      ],
      [
        { text: (gender === 'all' ? '✅ Both' : '👥 Both'), callback_data: `gen:${countryCode}:all:5` },
        { text: (gender === 'male' ? '✅ Male' : '👨 Male'), callback_data: `gen:${countryCode}:male:5` },
        { text: (gender === 'female' ? '✅ Female' : '👩 Female'), callback_data: `gen:${countryCode}:female:5` }
      ],
      [
        { text: '🌍 Choose Country', callback_data: 'home' },
        { text: '🔍 Search', callback_data: 'search_prompt' }
      ]
    ]
  };

  return { text, markup };
}

// Background Telegram Poller (Works on Hostinger Node.js automatically!)
let lastUpdateId = 0;
async function pollTelegram() {
  try {
    const res = await callTelegram('getUpdates', { offset: lastUpdateId + 1, timeout: 20 });
    if (res && res.ok && Array.isArray(res.result)) {
      for (const update of res.result) {
        lastUpdateId = update.update_id;
        handleUpdate(update);
      }
    }
  } catch (err) {
    // Silent catch, will retry
  }
  setTimeout(pollTelegram, 1000);
}

// Handle Incoming Telegram Updates
async function handleUpdate(u) {
  if (u.message) {
    const chat_id = u.message.chat.id;
    const text = (u.message.text || '').trim();

    if (text.startsWith('/start') || text.startsWith('/popular') || text.startsWith('/help')) {
      const welcome = `👋 <b>Nomix — কান্ট্রি র্যান্ডম নেম জেনারেটরে স্বাগতম!</b>\n\nবিশ্বের যেকোনো দেশের মানুষের কালচারাল নাম জেনারেট করুন আনলিমিটেড।\n\n👇 দেশ সিলেক্ট করুন অথবা <b>🔍 Search Country</b> চাপুন:`;
      await callTelegram('sendMessage', {
        chat_id,
        text: welcome,
        parse_mode: 'HTML',
        reply_markup: buildCountryKeyboard(1)
      });
    } else if (text.startsWith('/search')) {
      const q = text.replace('/search', '').trim();
      if (!q) {
        await callTelegram('sendMessage', {
          chat_id,
          text: '🔍 যে দেশের নাম চান লিখে মেসেজ পাঠান (যেমন: <code>Bangladesh</code>, <code>USA</code>, <code>bd</code>):',
          parse_mode: 'HTML'
        });
      } else {
        const results = searchCountries(q);
        await callTelegram('sendMessage', {
          chat_id,
          text: `🔍 '<b>${q}</b>' এর জন্য ফলাফল (${results.length} টি দেশ):`,
          parse_mode: 'HTML',
          reply_markup: buildCountryKeyboard(1, q)
        });
      }
    } else {
      // Treat text as search
      const results = searchCountries(text);
      if (results.length > 0) {
        await callTelegram('sendMessage', {
          chat_id,
          text: `🔍 '<b>${text}</b>' এর জন্য ফলাফল (${results.length} টি দেশ):`,
          parse_mode: 'HTML',
          reply_markup: buildCountryKeyboard(1, text)
        });
      } else {
        await callTelegram('sendMessage', {
          chat_id,
          text: `🔍 '<b>${text}</b>' নামে কোনো দেশ পাওয়া যায়নি। সঠিক নাম লিখে চেষ্টা করুন:`,
          parse_mode: 'HTML',
          reply_markup: buildCountryKeyboard(1)
        });
      }
    }
  } else if (u.callback_query) {
    const cq = u.callback_query;
    const chat_id = cq.message.chat.id;
    const message_id = cq.message.message_id;
    const data = cq.data;

    await callTelegram('answerCallbackQuery', { callback_query_id: cq.id });

    if (data === 'noop') return;

    if (data === 'home') {
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: '🌍 <b>যে দেশের নাম জেনারেট করতে চান সিলেক্ট করুন:</b>',
        parse_mode: 'HTML',
        reply_markup: buildCountryKeyboard(1)
      });
    } else if (data === 'search_prompt') {
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: '🔍 <b>দেশ সার্চ করুন:</b>\n\nদেশের নাম বা কোড লিখে মেসেজ পাঠান (যেমন: <code>bd</code>, <code>USA</code>, <code>Japan</code>, <code>Germany</code>):',
        parse_mode: 'HTML',
        reply_markup: { inline_keyboard: [[{ text: '🔙 Back to List', callback_data: 'home' }]] }
      });
    } else if (data.startsWith('page:')) {
      const page = parseInt(data.split(':')[1], 10);
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: '🌍 <b>সব দেশের তালিকা (পৃষ্ঠা পরিবর্তন):</b>',
        parse_mode: 'HTML',
        reply_markup: buildCountryKeyboard(page)
      });
    } else if (data.startsWith('sq:')) {
      const [, q, page] = data.split(':');
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: `🔍 '<b>${q}</b>' এর ফলাফল:`,
        parse_mode: 'HTML',
        reply_markup: buildCountryKeyboard(parseInt(page, 10), q)
      });
    } else if (data.startsWith('sel:')) {
      const code = data.split(':')[1];
      const screen = renderCountryScreen(code, 'all', 5);
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: screen.text,
        parse_mode: 'HTML',
        reply_markup: screen.markup
      });
    } else if (data.startsWith('gen:')) {
      const [, code, gender, count] = data.split(':');
      const screen = renderCountryScreen(code, gender, parseInt(count, 10));
      await callTelegram('editMessageText', {
        chat_id, message_id,
        text: screen.text,
        parse_mode: 'HTML',
        reply_markup: screen.markup
      });
    }
  }
}

// Start Server and Poller
app.listen(PORT, () => {
  console.log(`🚀 Nomix Web & Telegram Engine running on port ${PORT}`);
  pollTelegram();
});

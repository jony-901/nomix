"""
Comprehensive database of 195+ worldwide countries with ISO codes,
flag emojis, common aliases, and cultural name-pool mappings.
"""

from typing import Dict, List, Optional, TypedDict


class Country(TypedDict):
    code: str
    name: str
    flag: str
    pool: str
    aliases: List[str]


# Every entry maps a country to its ISO-3166-1 alpha-2 code, display name,
# flag emoji, cultural name pool key, and common search aliases.
COUNTRIES: List[Country] = [
    {"code": "AF", "name": "Afghanistan", "flag": "🇦🇫", "pool": "persian_afghan", "aliases": ["afg"]},
    {"code": "AL", "name": "Albania", "flag": "🇦🇱", "pool": "albanian", "aliases": ["alb"]},
    {"code": "DZ", "name": "Algeria", "flag": "🇩🇿", "pool": "maghreb_arabic", "aliases": ["dza"]},
    {"code": "AD", "name": "Andorra", "flag": "🇦🇩", "pool": "iberian_spanish", "aliases": ["and"]},
    {"code": "AO", "name": "Angola", "flag": "🇦🇴", "pool": "lusophone_african", "aliases": ["ago"]},
    {"code": "AG", "name": "Antigua and Barbuda", "flag": "🇦🇬", "pool": "caribbean_anglo", "aliases": ["antigua"]},
    {"code": "AR", "name": "Argentina", "flag": "🇦🇷", "pool": "hispanic_latam", "aliases": ["arg"]},
    {"code": "AM", "name": "Armenia", "flag": "🇦🇲", "pool": "armenian", "aliases": ["arm"]},
    {"code": "AU", "name": "Australia", "flag": "🇦🇺", "pool": "anglo_western", "aliases": ["aus", "aussie"]},
    {"code": "AT", "name": "Austria", "flag": "🇦🇹", "pool": "germanic", "aliases": ["aut"]},
    {"code": "AZ", "name": "Azerbaijan", "flag": "🇦🇿", "pool": "turkic_caucasus", "aliases": ["aze"]},
    {"code": "BS", "name": "Bahamas", "flag": "🇧🇸", "pool": "caribbean_anglo", "aliases": ["bhs"]},
    {"code": "BH", "name": "Bahrain", "flag": "🇧🇭", "pool": "gulf_arabic", "aliases": ["bhr"]},
    {"code": "BD", "name": "Bangladesh", "flag": "🇧🇩", "pool": "bangladeshi", "aliases": ["bd", "bangla", "bgd"]},
    {"code": "BB", "name": "Barbados", "flag": "🇧🇧", "pool": "caribbean_anglo", "aliases": ["brb"]},
    {"code": "BY", "name": "Belarus", "flag": "🇧🇾", "pool": "east_slavic", "aliases": ["blr"]},
    {"code": "BE", "name": "Belgium", "flag": "🇧🇪", "pool": "benelux", "aliases": ["bel"]},
    {"code": "BZ", "name": "Belize", "flag": "🇧🇿", "pool": "hispanic_latam", "aliases": ["blz"]},
    {"code": "BJ", "name": "Benin", "flag": "🇧🇯", "pool": "west_african_franco", "aliases": ["ben"]},
    {"code": "BT", "name": "Bhutan", "flag": "🇧🇹", "pool": "himalayan", "aliases": ["btn"]},
    {"code": "BO", "name": "Bolivia", "flag": "🇧🇴", "pool": "hispanic_latam", "aliases": ["bol"]},
    {"code": "BA", "name": "Bosnia and Herzegovina", "flag": "🇧🇦", "pool": "south_slavic", "aliases": ["bosnia", "bih"]},
    {"code": "BW", "name": "Botswana", "flag": "🇧🇼", "pool": "southern_african", "aliases": ["bwa"]},
    {"code": "BR", "name": "Brazil", "flag": "🇧🇷", "pool": "brazilian", "aliases": ["bra", "brasil"]},
    {"code": "BN", "name": "Brunei", "flag": "🇧🇳", "pool": "malay", "aliases": ["brn"]},
    {"code": "BG", "name": "Bulgaria", "flag": "🇧🇬", "pool": "south_slavic", "aliases": ["bgr"]},
    {"code": "BF", "name": "Burkina Faso", "flag": "🇧🇫", "pool": "west_african_franco", "aliases": ["bfa"]},
    {"code": "BI", "name": "Burundi", "flag": "🇧🇮", "pool": "east_african", "aliases": ["bdi"]},
    {"code": "CV", "name": "Cabo Verde", "flag": "🇨🇻", "pool": "lusophone_african", "aliases": ["cape verde", "cpv"]},
    {"code": "KH", "name": "Cambodia", "flag": "🇰🇭", "pool": "southeast_asian_khmer", "aliases": ["khm"]},
    {"code": "CM", "name": "Cameroon", "flag": "🇨🇲", "pool": "west_african_franco", "aliases": ["cmr"]},
    {"code": "CA", "name": "Canada", "flag": "🇨🇦", "pool": "anglo_western", "aliases": ["can"]},
    {"code": "CF", "name": "Central African Republic", "flag": "🇨🇫", "pool": "west_african_franco", "aliases": ["car", "caf"]},
    {"code": "TD", "name": "Chad", "flag": "🇹🇩", "pool": "sahel_african", "aliases": ["tcd"]},
    {"code": "CL", "name": "Chile", "flag": "🇨🇱", "pool": "hispanic_latam", "aliases": ["chl"]},
    {"code": "CN", "name": "China", "flag": "🇨🇳", "pool": "chinese", "aliases": ["chn", "prc"]},
    {"code": "CO", "name": "Colombia", "flag": "🇨🇴", "pool": "hispanic_latam", "aliases": ["col"]},
    {"code": "KM", "name": "Comoros", "flag": "🇰🇲", "pool": "east_african", "aliases": ["com"]},
    {"code": "CG", "name": "Congo", "flag": "🇨🇬", "pool": "west_african_franco", "aliases": ["republic of congo", "cog"]},
    {"code": "CD", "name": "Congo (DRC)", "flag": "🇨🇩", "pool": "west_african_franco", "aliases": ["drc", "dr congo", "cod"]},
    {"code": "CR", "name": "Costa Rica", "flag": "🇨🇷", "pool": "hispanic_latam", "aliases": ["cri"]},
    {"code": "CI", "name": "Côte d'Ivoire", "flag": "🇨🇮", "pool": "west_african_franco", "aliases": ["ivory coast", "civ"]},
    {"code": "HR", "name": "Croatia", "flag": "🇭🇷", "pool": "south_slavic", "aliases": ["hrv"]},
    {"code": "CU", "name": "Cuba", "flag": "🇨🇺", "pool": "hispanic_latam", "aliases": ["cub"]},
    {"code": "CY", "name": "Cyprus", "flag": "🇨🇾", "pool": "greek", "aliases": ["cyp"]},
    {"code": "CZ", "name": "Czechia", "flag": "🇨🇿", "pool": "west_slavic", "aliases": ["czech republic", "cze"]},
    {"code": "DK", "name": "Denmark", "flag": "🇩🇰", "pool": "nordic", "aliases": ["dnk"]},
    {"code": "DJ", "name": "Djibouti", "flag": "🇩🇯", "pool": "horn_african", "aliases": ["dji"]},
    {"code": "DM", "name": "Dominica", "flag": "🇩🇲", "pool": "caribbean_anglo", "aliases": ["dma"]},
    {"code": "DO", "name": "Dominican Republic", "flag": "🇩🇴", "pool": "hispanic_latam", "aliases": ["dom"]},
    {"code": "EC", "name": "Ecuador", "flag": "🇪🇨", "pool": "hispanic_latam", "aliases": ["ecu"]},
    {"code": "EG", "name": "Egypt", "flag": "🇪🇬", "pool": "egyptian_arabic", "aliases": ["egy"]},
    {"code": "SV", "name": "El Salvador", "flag": "🇸🇻", "pool": "hispanic_latam", "aliases": ["slv"]},
    {"code": "GQ", "name": "Equatorial Guinea", "flag": "🇬🇶", "pool": "hispanic_latam", "aliases": ["gnq"]},
    {"code": "ER", "name": "Eritrea", "flag": "🇪🇷", "pool": "horn_african", "aliases": ["eri"]},
    {"code": "EE", "name": "Estonia", "flag": "🇪🇪", "pool": "baltic_finnic", "aliases": ["est"]},
    {"code": "SZ", "name": "Eswatini", "flag": "🇸🇿", "pool": "southern_african", "aliases": ["swaziland", "swz"]},
    {"code": "ET", "name": "Ethiopia", "flag": "🇪🇹", "pool": "horn_african", "aliases": ["eth"]},
    {"code": "FJ", "name": "Fiji", "flag": "🇫🇯", "pool": "pacific_polynesian", "aliases": ["fji"]},
    {"code": "FI", "name": "Finland", "flag": "🇫🇮", "pool": "finnish", "aliases": ["fin"]},
    {"code": "FR", "name": "France", "flag": "🇫🇷", "pool": "french", "aliases": ["fra"]},
    {"code": "GA", "name": "Gabon", "flag": "🇬🇦", "pool": "west_african_franco", "aliases": ["gab"]},
    {"code": "GM", "name": "Gambia", "flag": "🇬🇲", "pool": "west_african_anglo", "aliases": ["gmb"]},
    {"code": "GE", "name": "Georgia", "flag": "🇬🇪", "pool": "georgian", "aliases": ["geo"]},
    {"code": "DE", "name": "Germany", "flag": "🇩🇪", "pool": "germanic", "aliases": ["deu", "ger", "deutschland"]},
    {"code": "GH", "name": "Ghana", "flag": "🇬🇭", "pool": "west_african_anglo", "aliases": ["gha"]},
    {"code": "GR", "name": "Greece", "flag": "🇬🇷", "pool": "greek", "aliases": ["grc"]},
    {"code": "GD", "name": "Grenada", "flag": "🇬🇩", "pool": "caribbean_anglo", "aliases": ["grd"]},
    {"code": "GT", "name": "Guatemala", "flag": "🇬🇹", "pool": "hispanic_latam", "aliases": ["gtm"]},
    {"code": "GN", "name": "Guinea", "flag": "🇬🇳", "pool": "west_african_franco", "aliases": ["gin"]},
    {"code": "GW", "name": "Guinea-Bissau", "flag": "🇬🇼", "pool": "lusophone_african", "aliases": ["gnb"]},
    {"code": "GY", "name": "Guyana", "flag": "🇬🇾", "pool": "caribbean_anglo", "aliases": ["guy"]},
    {"code": "HT", "name": "Haiti", "flag": "🇭🇹", "pool": "french", "aliases": ["hti"]},
    {"code": "HN", "name": "Honduras", "flag": "🇭🇳", "pool": "hispanic_latam", "aliases": ["hnd"]},
    {"code": "HU", "name": "Hungary", "flag": "🇭🇺", "pool": "hungarian", "aliases": ["hun"]},
    {"code": "IS", "name": "Iceland", "flag": "🇮🇸", "pool": "nordic", "aliases": ["isl"]},
    {"code": "IN", "name": "India", "flag": "🇮🇳", "pool": "indian", "aliases": ["ind", "bharat"]},
    {"code": "ID", "name": "Indonesia", "flag": "🇮🇩", "pool": "indonesian", "aliases": ["idn", "indo"]},
    {"code": "IR", "name": "Iran", "flag": "🇮🇷", "pool": "persian_afghan", "aliases": ["irn", "persia"]},
    {"code": "IQ", "name": "Iraq", "flag": "🇮🇶", "pool": "levant_arabic", "aliases": ["irq"]},
    {"code": "IE", "name": "Ireland", "flag": "🇮🇪", "pool": "irish_celtic", "aliases": ["irl"]},
    {"code": "IL", "name": "Israel", "flag": "🇮🇱", "pool": "hebrew", "aliases": ["isr"]},
    {"code": "IT", "name": "Italy", "flag": "🇮🇹", "pool": "italian", "aliases": ["ita"]},
    {"code": "JM", "name": "Jamaica", "flag": "🇯🇲", "pool": "caribbean_anglo", "aliases": ["jam"]},
    {"code": "JP", "name": "Japan", "flag": "🇯🇵", "pool": "japanese", "aliases": ["jpn"]},
    {"code": "JO", "name": "Jordan", "flag": "🇯🇴", "pool": "levant_arabic", "aliases": ["jor"]},
    {"code": "KZ", "name": "Kazakhstan", "flag": "🇰🇿", "pool": "central_asian_turkic", "aliases": ["kaz"]},
    {"code": "KE", "name": "Kenya", "flag": "🇰🇪", "pool": "east_african", "aliases": ["ken"]},
    {"code": "KI", "name": "Kiribati", "flag": "🇰🇮", "pool": "pacific_polynesian", "aliases": ["kir"]},
    {"code": "KP", "name": "North Korea", "flag": "🇰🇵", "pool": "korean", "aliases": ["dprk", "prk"]},
    {"code": "KR", "name": "South Korea", "flag": "🇰🇷", "pool": "korean", "aliases": ["korea", "kor", "rok"]},
    {"code": "KW", "name": "Kuwait", "flag": "🇰🇼", "pool": "gulf_arabic", "aliases": ["kwt"]},
    {"code": "KG", "name": "Kyrgyzstan", "flag": "🇰🇬", "pool": "central_asian_turkic", "aliases": ["kgz"]},
    {"code": "LA", "name": "Laos", "flag": "🇱🇦", "pool": "southeast_asian_thai_lao", "aliases": ["lao"]},
    {"code": "LV", "name": "Latvia", "flag": "🇱🇻", "pool": "baltic_finnic", "aliases": ["lva"]},
    {"code": "LB", "name": "Lebanon", "flag": "🇱🇧", "pool": "levant_arabic", "aliases": ["lbn"]},
    {"code": "LS", "name": "Lesotho", "flag": "🇱🇸", "pool": "southern_african", "aliases": ["lso"]},
    {"code": "LR", "name": "Liberia", "flag": "🇱🇷", "pool": "west_african_anglo", "aliases": ["lbr"]},
    {"code": "LY", "name": "Libya", "flag": "🇱🇾", "pool": "maghreb_arabic", "aliases": ["lby"]},
    {"code": "LI", "name": "Liechtenstein", "flag": "🇱🇮", "pool": "germanic", "aliases": ["lie"]},
    {"code": "LT", "name": "Lithuania", "flag": "🇱🇹", "pool": "baltic_finnic", "aliases": ["ltu"]},
    {"code": "LU", "name": "Luxembourg", "flag": "🇱🇺", "pool": "benelux", "aliases": ["lux"]},
    {"code": "MG", "name": "Madagascar", "flag": "🇲🇬", "pool": "east_african", "aliases": ["mdg"]},
    {"code": "MW", "name": "Malawi", "flag": "🇲🇼", "pool": "southern_african", "aliases": ["mwi"]},
    {"code": "MY", "name": "Malaysia", "flag": "🇲🇾", "pool": "malay", "aliases": ["mys"]},
    {"code": "MV", "name": "Maldives", "flag": "🇲🇻", "pool": "south_asian_island", "aliases": ["mdv"]},
    {"code": "ML", "name": "Mali", "flag": "🇲🇱", "pool": "sahel_african", "aliases": ["mli"]},
    {"code": "MT", "name": "Malta", "flag": "🇲🇹", "pool": "italian", "aliases": ["mlt"]},
    {"code": "MH", "name": "Marshall Islands", "flag": "🇲🇭", "pool": "pacific_polynesian", "aliases": ["mhl"]},
    {"code": "MR", "name": "Mauritania", "flag": "🇲🇷", "pool": "maghreb_arabic", "aliases": ["mrt"]},
    {"code": "MU", "name": "Mauritius", "flag": "🇲🇺", "pool": "indian", "aliases": ["mus"]},
    {"code": "MX", "name": "Mexico", "flag": "🇲🇽", "pool": "hispanic_latam", "aliases": ["mex"]},
    {"code": "FM", "name": "Micronesia", "flag": "🇫🇲", "pool": "pacific_polynesian", "aliases": ["fsm"]},
    {"code": "MD", "name": "Moldova", "flag": "🇲🇩", "pool": "romanian", "aliases": ["mda"]},
    {"code": "MC", "name": "Monaco", "flag": "🇲🇨", "pool": "french", "aliases": ["mco"]},
    {"code": "MN", "name": "Mongolia", "flag": "🇲🇳", "pool": "mongolian", "aliases": ["mng"]},
    {"code": "ME", "name": "Montenegro", "flag": "🇲🇪", "pool": "south_slavic", "aliases": ["mne"]},
    {"code": "MA", "name": "Morocco", "flag": "🇲🇦", "pool": "maghreb_arabic", "aliases": ["mar"]},
    {"code": "MZ", "name": "Mozambique", "flag": "🇲🇿", "pool": "lusophone_african", "aliases": ["moz"]},
    {"code": "MM", "name": "Myanmar", "flag": "🇲🇲", "pool": "myanmar", "aliases": ["burma", "mmr"]},
    {"code": "NA", "name": "Namibia", "flag": "🇳🇦", "pool": "southern_african", "aliases": ["nam"]},
    {"code": "NR", "name": "Nauru", "flag": "🇳🇷", "pool": "pacific_polynesian", "aliases": ["nru"]},
    {"code": "NP", "name": "Nepal", "flag": "🇳🇵", "pool": "nepali", "aliases": ["npl"]},
    {"code": "NL", "name": "Netherlands", "flag": "🇳🇱", "pool": "benelux", "aliases": ["holland", "nld"]},
    {"code": "NZ", "name": "New Zealand", "flag": "🇳🇿", "pool": "anglo_western", "aliases": ["nzl", "kiwi"]},
    {"code": "NI", "name": "Nicaragua", "flag": "🇳🇮", "pool": "hispanic_latam", "aliases": ["nic"]},
    {"code": "NE", "name": "Niger", "flag": "🇳🇪", "pool": "sahel_african", "aliases": ["ner"]},
    {"code": "NG", "name": "Nigeria", "flag": "🇳🇬", "pool": "nigerian", "aliases": ["nga"]},
    {"code": "MK", "name": "North Macedonia", "flag": "🇲🇰", "pool": "south_slavic", "aliases": ["macedonia", "mkd"]},
    {"code": "NO", "name": "Norway", "flag": "🇳🇴", "pool": "nordic", "aliases": ["nor"]},
    {"code": "OM", "name": "Oman", "flag": "🇴🇲", "pool": "gulf_arabic", "aliases": ["omn"]},
    {"code": "PK", "name": "Pakistan", "flag": "🇵🇰", "pool": "pakistani", "aliases": ["pak"]},
    {"code": "PW", "name": "Palau", "flag": "🇵🇼", "pool": "pacific_polynesian", "aliases": ["plw"]},
    {"code": "PS", "name": "Palestine", "flag": "🇵🇸", "pool": "levant_arabic", "aliases": ["pse"]},
    {"code": "PA", "name": "Panama", "flag": "🇵🇦", "pool": "hispanic_latam", "aliases": ["pan"]},
    {"code": "PG", "name": "Papua New Guinea", "flag": "🇵🇬", "pool": "pacific_polynesian", "aliases": ["png"]},
    {"code": "PY", "name": "Paraguay", "flag": "🇵🇾", "pool": "hispanic_latam", "aliases": ["pry"]},
    {"code": "PE", "name": "Peru", "flag": "🇵🇪", "pool": "hispanic_latam", "aliases": ["per"]},
    {"code": "PH", "name": "Philippines", "flag": "🇵🇭", "pool": "filipino", "aliases": ["phl"]},
    {"code": "PL", "name": "Poland", "flag": "🇵🇱", "pool": "west_slavic", "aliases": ["pol"]},
    {"code": "PT", "name": "Portugal", "flag": "🇵🇹", "pool": "iberian_portuguese", "aliases": ["prt"]},
    {"code": "QA", "name": "Qatar", "flag": "🇶🇦", "pool": "gulf_arabic", "aliases": ["qat"]},
    {"code": "RO", "name": "Romania", "flag": "🇷🇴", "pool": "romanian", "aliases": ["rou"]},
    {"code": "RU", "name": "Russia", "flag": "🇷🇺", "pool": "east_slavic", "aliases": ["rus"]},
    {"code": "RW", "name": "Rwanda", "flag": "🇷🇼", "pool": "east_african", "aliases": ["rwa"]},
    {"code": "KN", "name": "Saint Kitts and Nevis", "flag": "🇰🇳", "pool": "caribbean_anglo", "aliases": ["kna"]},
    {"code": "LC", "name": "Saint Lucia", "flag": "🇱🇨", "pool": "caribbean_anglo", "aliases": ["lca"]},
    {"code": "VC", "name": "Saint Vincent and the Grenadines", "flag": "🇻🇨", "pool": "caribbean_anglo", "aliases": ["vct"]},
    {"code": "WS", "name": "Samoa", "flag": "🇼🇸", "pool": "pacific_polynesian", "aliases": ["wsm"]},
    {"code": "SM", "name": "San Marino", "flag": "🇸🇲", "pool": "italian", "aliases": ["smr"]},
    {"code": "ST", "name": "Sao Tome and Principe", "flag": "🇸🇹", "pool": "lusophone_african", "aliases": ["stp"]},
    {"code": "SA", "name": "Saudi Arabia", "flag": "🇸🇦", "pool": "gulf_arabic", "aliases": ["ksa", "saudi", "sau"]},
    {"code": "SN", "name": "Senegal", "flag": "🇸🇳", "pool": "sahel_african", "aliases": ["sen"]},
    {"code": "RS", "name": "Serbia", "flag": "🇷🇸", "pool": "south_slavic", "aliases": ["srb"]},
    {"code": "SC", "name": "Seychelles", "flag": "🇸🇨", "pool": "east_african", "aliases": ["syc"]},
    {"code": "SL", "name": "Sierra Leone", "flag": "🇸🇱", "pool": "west_african_anglo", "aliases": ["sle"]},
    {"code": "SG", "name": "Singapore", "flag": "🇸🇬", "pool": "singaporean", "aliases": ["sgp"]},
    {"code": "SK", "name": "Slovakia", "flag": "🇸🇰", "pool": "west_slavic", "aliases": ["svk"]},
    {"code": "SI", "name": "Slovenia", "flag": "🇸🇮", "pool": "south_slavic", "aliases": ["svn"]},
    {"code": "SB", "name": "Solomon Islands", "flag": "🇸🇧", "pool": "pacific_polynesian", "aliases": ["slb"]},
    {"code": "SO", "name": "Somalia", "flag": "🇸🇴", "pool": "horn_african", "aliases": ["som"]},
    {"code": "ZA", "name": "South Africa", "flag": "🇿🇦", "pool": "southern_african", "aliases": ["zaf", "rsa"]},
    {"code": "SS", "name": "South Sudan", "flag": "🇸🇸", "pool": "east_african", "aliases": ["ssd"]},
    {"code": "ES", "name": "Spain", "flag": "🇪🇸", "pool": "iberian_spanish", "aliases": ["esp"]},
    {"code": "LK", "name": "Sri Lanka", "flag": "🇱🇰", "pool": "sri_lankan", "aliases": ["lka"]},
    {"code": "SD", "name": "Sudan", "flag": "🇸🇩", "pool": "egyptian_arabic", "aliases": ["sdn"]},
    {"code": "SR", "name": "Suriname", "flag": "🇸🇷", "pool": "benelux", "aliases": ["sur"]},
    {"code": "SE", "name": "Sweden", "flag": "🇸🇪", "pool": "nordic", "aliases": ["swe"]},
    {"code": "CH", "name": "Switzerland", "flag": "🇨🇭", "pool": "germanic", "aliases": ["che", "swiss"]},
    {"code": "SY", "name": "Syria", "flag": "🇸🇾", "pool": "levant_arabic", "aliases": ["syr"]},
    {"code": "TW", "name": "Taiwan", "flag": "🇹🇼", "pool": "chinese", "aliases": ["twn"]},
    {"code": "TJ", "name": "Tajikistan", "flag": "🇹🇯", "pool": "persian_afghan", "aliases": ["tjk"]},
    {"code": "TZ", "name": "Tanzania", "flag": "🇹🇿", "pool": "east_african", "aliases": ["tza"]},
    {"code": "TH", "name": "Thailand", "flag": "🇹🇭", "pool": "southeast_asian_thai_lao", "aliases": ["tha"]},
    {"code": "TL", "name": "Timor-Leste", "flag": "🇹🇱", "pool": "indonesian", "aliases": ["east timor", "tls"]},
    {"code": "TG", "name": "Togo", "flag": "🇹🇬", "pool": "west_african_franco", "aliases": ["tgo"]},
    {"code": "TO", "name": "Tonga", "flag": "🇹🇴", "pool": "pacific_polynesian", "aliases": ["ton"]},
    {"code": "TT", "name": "Trinidad and Tobago", "flag": "🇹🇹", "pool": "caribbean_anglo", "aliases": ["tto"]},
    {"code": "TN", "name": "Tunisia", "flag": "🇹🇳", "pool": "maghreb_arabic", "aliases": ["tun"]},
    {"code": "TR", "name": "Turkey", "flag": "🇹🇷", "pool": "turkish", "aliases": ["turkiye", "tur"]},
    {"code": "TM", "name": "Turkmenistan", "flag": "🇹🇲", "pool": "central_asian_turkic", "aliases": ["tkm"]},
    {"code": "TV", "name": "Tuvalu", "flag": "🇹🇻", "pool": "pacific_polynesian", "aliases": ["tuv"]},
    {"code": "UG", "name": "Uganda", "flag": "🇺🇬", "pool": "east_african", "aliases": ["uga"]},
    {"code": "UA", "name": "Ukraine", "flag": "🇺🇦", "pool": "east_slavic", "aliases": ["ukr"]},
    {"code": "AE", "name": "United Arab Emirates", "flag": "🇦🇪", "pool": "gulf_arabic", "aliases": ["uae", "dubai", "are"]},
    {"code": "GB", "name": "United Kingdom", "flag": "🇬🇧", "pool": "anglo_western", "aliases": ["uk", "britain", "england", "gbr"]},
    {"code": "US", "name": "United States", "flag": "🇺🇸", "pool": "anglo_western", "aliases": ["usa", "us", "america"]},
    {"code": "UY", "name": "Uruguay", "flag": "🇺🇾", "pool": "hispanic_latam", "aliases": ["ury"]},
    {"code": "UZ", "name": "Uzbekistan", "flag": "🇺🇿", "pool": "central_asian_turkic", "aliases": ["uzb"]},
    {"code": "VU", "name": "Vanuatu", "flag": "🇻🇺", "pool": "pacific_polynesian", "aliases": ["vut"]},
    {"code": "VA", "name": "Vatican City", "flag": "🇻🇦", "pool": "italian", "aliases": ["vat"]},
    {"code": "VE", "name": "Venezuela", "flag": "🇻🇪", "pool": "hispanic_latam", "aliases": ["ven"]},
    {"code": "VN", "name": "Vietnam", "flag": "🇻🇳", "pool": "vietnamese", "aliases": ["vnm"]},
    {"code": "YE", "name": "Yemen", "flag": "🇾🇪", "pool": "gulf_arabic", "aliases": ["yem"]},
    {"code": "ZM", "name": "Zambia", "flag": "🇿🇲", "pool": "southern_african", "aliases": ["zmb"]},
    {"code": "ZW", "name": "Zimbabwe", "flag": "🇿🇼", "pool": "southern_african", "aliases": ["zwe"]},
]

COUNTRY_BY_CODE: Dict[str, Country] = {c["code"]: c for c in COUNTRIES}


def get_country_by_code(code: str) -> Optional[Country]:
    """Return a country dict by its 2-letter ISO code."""
    return COUNTRY_BY_CODE.get(code.upper())


def search_countries(query: str) -> List[Country]:
    """
    Search countries by name, ISO code, or alias.
    Exact and prefix matches are ranked before substring matches.
    """
    q = query.strip().lower()
    if not q:
        return []

    exact: List[Country] = []
    prefix: List[Country] = []
    substring: List[Country] = []

    for c in COUNTRIES:
        name_l = c["name"].lower()
        code_l = c["code"].lower()
        aliases_l = [a.lower() for a in c["aliases"]]

        if q == name_l or q == code_l or q in aliases_l:
            exact.append(c)
        elif name_l.startswith(q) or any(a.startswith(q) for a in aliases_l):
            prefix.append(c)
        elif q in name_l or any(q in a for a in aliases_l):
            substring.append(c)

    return exact + prefix + substring

/**
 * Worldwide Country Random Name Generator - Frontend Core Logic
 * Fast Workflow: Recents + Wishlist + Flexible Quantity Selection
 */

const FEATURED_CODES = ["BD", "US", "GB", "IN", "JP", "DE"];
const PAGE_SIZE = 6;
const MAX_RECENTS = 8;

// LocalStorage Keys
const STORAGE_KEYS = {
  RECENTS: 'wng_recents',
  WISHLIST: 'wng_wishlist',
  LAST_QTY: 'wng_last_qty',
  LAST_GENDER: 'wng_last_gender'
};

// Application State
const state = {
  allCountries: [],
  filteredCountries: [],
  currentPage: 1,
  selectedCountry: null,
  activeGender: localStorage.getItem(STORAGE_KEYS.LAST_GENDER) || 'all',
  nameCount: parseInt(localStorage.getItem(STORAGE_KEYS.LAST_QTY), 10) || 5,
  isFeaturedOnly: true,
  recents: [],
  wishlist: []
};

// DOM Elements
const countrySearch = document.getElementById('countrySearch');
const clearSearchBtn = document.getElementById('clearSearchBtn');
const resultsCount = document.getElementById('resultsCount');
const resetViewBtn = document.getElementById('resetViewBtn');
const allCountriesBtn = document.getElementById('allCountriesBtn');
const countryGrid = document.getElementById('countryGrid');
const paginationBar = document.getElementById('paginationBar');
const prevPageBtn = document.getElementById('prevPageBtn');
const nextPageBtn = document.getElementById('nextPageBtn');
const pageIndicator = document.getElementById('pageIndicator');

// Quick Hub Elements
const recentChips = document.getElementById('recentChips');
const wishlistChips = document.getElementById('wishlistChips');
const batchWishlistBtn = document.getElementById('batchWishlistBtn');

// Generator Panel Elements
const generatorSection = document.getElementById('generatorSection');
const genFlag = document.getElementById('genFlag');
const genCountryName = document.getElementById('genCountryName');
const genSubText = document.getElementById('genSubText');
const toggleWishlistBtn = document.getElementById('toggleWishlistBtn');
const closeGenBtn = document.getElementById('closeGenBtn');
const generateBtn = document.getElementById('generateBtn');
const copyAllBtn = document.getElementById('copyAllBtn');
const copyNotice = document.getElementById('copyNotice');
const nameResultsList = document.getElementById('nameResultsList');
const resultsCountNotice = document.getElementById('resultsCountNotice');
const genderButtons = document.querySelectorAll('.seg-btn');
const qtyButtons = document.querySelectorAll('.qty-btn');
const customQtyInput = document.getElementById('customQtyInput');

// Batch Multi-Country Elements
const batchResultsSection = document.getElementById('batchResultsSection');
const closeBatchBtn = document.getElementById('closeBatchBtn');
const batchRegenBtn = document.getElementById('batchRegenBtn');
const copyAllBatchBtn = document.getElementById('copyAllBatchBtn');
const batchContainer = document.getElementById('batchContainer');

/**
 * Initialize Application
 */
function init() {
  if (typeof DATA === 'undefined' || !DATA.countries) {
    console.error('DATA object not found. Ensure data.js is loaded.');
    return;
  }

  // Load persistence
  loadStorage();

  // Pre-sort countries: featured first, then others
  const featuredList = [];
  const otherList = [];

  DATA.countries.forEach(c => {
    if (FEATURED_CODES.includes(c.code)) {
      featuredList.push(c);
    } else {
      otherList.push(c);
    }
  });

  state.allCountries = [...featuredList, ...otherList];
  setFeaturedView();

  // Restore saved gender & quantity buttons UI
  restoreSavedPreferences();

  // Render Hub
  renderRecentsHub();
  renderWishlistHub();

  setupEventListeners();
}

/**
 * Storage Helpers
 */
function loadStorage() {
  try {
    state.recents = JSON.parse(localStorage.getItem(STORAGE_KEYS.RECENTS) || '[]');
    state.wishlist = JSON.parse(localStorage.getItem(STORAGE_KEYS.WISHLIST) || '[]');
  } catch (e) {
    state.recents = [];
    state.wishlist = [];
  }
}

function saveStorage() {
  localStorage.setItem(STORAGE_KEYS.RECENTS, JSON.stringify(state.recents));
  localStorage.setItem(STORAGE_KEYS.WISHLIST, JSON.stringify(state.wishlist));
  localStorage.setItem(STORAGE_KEYS.LAST_QTY, state.nameCount);
  localStorage.setItem(STORAGE_KEYS.LAST_GENDER, state.activeGender);
}

function restoreSavedPreferences() {
  // Gender buttons
  genderButtons.forEach(btn => {
    if (btn.getAttribute('data-gender') === state.activeGender) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Qty buttons
  let matched = false;
  qtyButtons.forEach(btn => {
    if (parseInt(btn.getAttribute('data-qty'), 10) === state.nameCount) {
      btn.classList.add('active');
      matched = true;
    } else {
      btn.classList.remove('active');
    }
  });

  if (!matched && state.nameCount) {
    customQtyInput.value = state.nameCount;
  }
}

/**
 * Add to Recents
 */
function pushToRecents(country) {
  state.recents = state.recents.filter(c => c.code !== country.code);
  state.recents.unshift({ code: country.code, name: country.name, flag: country.flag });
  if (state.recents.length > MAX_RECENTS) {
    state.recents.pop();
  }
  saveStorage();
  renderRecentsHub();
}

/**
 * Toggle Wishlist
 */
function toggleWishlist(country) {
  const index = state.wishlist.findIndex(c => c.code === country.code);
  if (index >= 0) {
    state.wishlist.splice(index, 1);
  } else {
    state.wishlist.push({ code: country.code, name: country.name, flag: country.flag, pool: country.pool });
  }
  saveStorage();
  renderWishlistHub();
  updateWishlistUI();
  renderGrid(); // updates stars on cards
}

function isInWishlist(code) {
  return state.wishlist.some(c => c.code === code);
}

function updateWishlistUI() {
  if (!state.selectedCountry) return;
  const isWish = isInWishlist(state.selectedCountry.code);
  if (isWish) {
    toggleWishlistBtn.classList.add('active');
    toggleWishlistBtn.innerHTML = '★ In Wishlist';
  } else {
    toggleWishlistBtn.classList.remove('active');
    toggleWishlistBtn.innerHTML = '⭐ Wishlist';
  }
}

/**
 * Render Quick Hub (Recents & Wishlist chips)
 */
function renderRecentsHub() {
  if (state.recents.length === 0) {
    recentChips.innerHTML = '<span class="empty-hint">এখনো কোনো রিসেন্ট দেশ নেই (একটি দেশ সিলেক্ট করলেই এখানে সেভ হয়ে যাবে)</span>';
    return;
  }

  recentChips.innerHTML = '';
  state.recents.forEach(item => {
    const chip = document.createElement('button');
    chip.className = 'quick-chip';
    chip.innerHTML = `<span>${item.flag}</span> <span>${item.name}</span>`;
    chip.addEventListener('click', () => {
      const fullCountry = state.allCountries.find(c => c.code === item.code);
      if (fullCountry) selectCountry(fullCountry);
    });
    recentChips.appendChild(chip);
  });
}

function renderWishlistHub() {
  if (state.wishlist.length === 0) {
    wishlistChips.innerHTML = '<span class="empty-hint">উইশলিস্ট খালি। নিচের দেশের কার্ড থেকে ⭐ বাটনে চাপ দিয়ে অ্যাড করুন।</span>';
    batchWishlistBtn.style.display = 'none';
    return;
  }

  batchWishlistBtn.style.display = 'inline-block';
  wishlistChips.innerHTML = '';
  state.wishlist.forEach(item => {
    const chip = document.createElement('div');
    chip.className = 'quick-chip wishlist-chip';
    chip.innerHTML = `
      <span style="cursor:pointer;" class="chip-click"><span>${item.flag}</span> <span>${item.name}</span></span>
      <button class="chip-remove-btn" title="উইশলিস্ট থেকে মুছুন">✕</button>
    `;

    chip.querySelector('.chip-click').addEventListener('click', () => {
      const fullCountry = state.allCountries.find(c => c.code === item.code);
      if (fullCountry) selectCountry(fullCountry);
    });

    chip.querySelector('.chip-remove-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      toggleWishlist(item);
    });

    wishlistChips.appendChild(chip);
  });
}

/**
 * Set view to featured top 6 countries
 */
function setFeaturedView() {
  state.isFeaturedOnly = true;
  state.filteredCountries = state.allCountries.filter(c => FEATURED_CODES.includes(c.code));
  state.currentPage = 1;

  resetViewBtn.classList.add('active');
  allCountriesBtn.classList.remove('active');
  renderGrid();
}

/**
 * Set view to all 196 countries
 */
function setAllCountriesView() {
  state.isFeaturedOnly = false;
  state.filteredCountries = [...state.allCountries];
  state.currentPage = 1;

  allCountriesBtn.classList.add('active');
  resetViewBtn.classList.remove('active');
  renderGrid();
}

/**
 * Search logic
 */
function handleSearch(query) {
  const q = query.trim().toLowerCase();
  if (!q) {
    clearSearchBtn.style.display = 'none';
    if (state.isFeaturedOnly) {
      setFeaturedView();
    } else {
      setAllCountriesView();
    }
    return;
  }

  clearSearchBtn.style.display = 'block';
  resetViewBtn.classList.remove('active');
  allCountriesBtn.classList.remove('active');

  const exact = [];
  const prefix = [];
  const substring = [];

  state.allCountries.forEach(c => {
    const nameL = c.name.toLowerCase();
    const codeL = c.code.toLowerCase();
    const aliases = (c.aliases || []).map(a => a.toLowerCase());

    if (nameL === q || codeL === q || aliases.includes(q)) {
      exact.push(c);
    } else if (nameL.startsWith(q) || codeL.startsWith(q) || aliases.some(a => a.startsWith(q))) {
      prefix.push(c);
    } else if (nameL.includes(q) || aliases.some(a => a.includes(q))) {
      substring.push(c);
    }
  });

  state.filteredCountries = [...exact, ...prefix, ...substring];
  state.currentPage = 1;
  renderGrid();
}

/**
 * Render the country grid and update pagination
 */
function renderGrid() {
  const total = state.filteredCountries.length;
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));
  state.currentPage = Math.max(1, Math.min(state.currentPage, totalPages));

  resultsCount.textContent = `Showing ${total} ${total === 1 ? 'country' : 'countries'}`;

  const start = (state.currentPage - 1) * PAGE_SIZE;
  const pageItems = state.filteredCountries.slice(start, start + PAGE_SIZE);

  countryGrid.innerHTML = '';

  if (pageItems.length === 0) {
    countryGrid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 40px 20px; color: #94a3b8;">
        <p style="font-size: 1.8rem; margin-bottom: 8px;">🔍</p>
        <p style="font-weight: 600;">No countries found matching your search.</p>
        <p style="font-size: 0.85rem; margin-top: 4px;">Try searching by country name or code (e.g. BD, USA, Japan).</p>
      </div>
    `;
    paginationBar.style.display = 'none';
    return;
  }

  pageItems.forEach(country => {
    const isWish = isInWishlist(country.code);
    const card = document.createElement('div');
    card.className = `country-card ${state.selectedCountry && state.selectedCountry.code === country.code ? 'selected' : ''}`;
    
    card.innerHTML = `
      <div class="c-main">
        <span class="c-flag">${country.flag}</span>
        <div class="c-info">
          <span class="c-name">${country.name}</span>
          <span class="c-sub">${country.code} • 1-Click Generate</span>
        </div>
      </div>
      <button class="card-star-btn ${isWish ? 'active' : ''}" title="${isWish ? 'Remove from Wishlist' : 'Add to Wishlist'}">
        ${isWish ? '★' : '☆'}
      </button>
    `;

    // Click on main body opens generator
    card.querySelector('.c-main').addEventListener('click', () => {
      selectCountry(country);
    });

    // Click on star toggles wishlist without triggering generator
    card.querySelector('.card-star-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      toggleWishlist(country);
    });

    countryGrid.appendChild(card);
  });

  if (totalPages > 1) {
    paginationBar.style.display = 'flex';
    pageIndicator.textContent = `Page ${state.currentPage} of ${totalPages}`;
    prevPageBtn.disabled = state.currentPage <= 1;
    nextPageBtn.disabled = state.currentPage >= totalPages;
  } else {
    paginationBar.style.display = 'none';
  }
}

/**
 * Select country, record in recents, and trigger generator
 */
function selectCountry(country) {
  state.selectedCountry = country;
  pushToRecents(country);

  // Close batch view if open
  batchResultsSection.style.display = 'none';

  renderGrid(); // update selected outline
  updateWishlistUI();

  genFlag.textContent = country.flag;
  genCountryName.textContent = country.name;
  genSubText.textContent = `ISO: ${country.code} • Cultural Pool: ${country.pool.replace(/_/g, ' ')}`;

  generatorSection.style.display = 'block';
  generatorSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

  generateNames();
}

/**
 * Random Name Generation Engine
 */
function generateNames() {
  if (!state.selectedCountry) return;

  const poolKey = state.selectedCountry.pool;
  const pool = DATA.pools[poolKey] || DATA.pools['anglo_western'];
  const count = state.nameCount || 5;
  const gender = state.activeGender;

  resultsCountNotice.textContent = `Generated ${count} Names (${gender.toUpperCase()})`;

  const maleNames = pool.male_first || [];
  const femaleNames = pool.female_first || [];
  const lastNames = pool.last_names || [];

  nameResultsList.innerHTML = '';
  const currentGenerated = [];

  for (let i = 0; i < count; i++) {
    let first = '';
    let icon = '';

    if (gender === 'male') {
      first = getRandomItem(maleNames);
      icon = '👨';
    } else if (gender === 'female') {
      first = getRandomItem(femaleNames);
      icon = '👩';
    } else {
      if (Math.random() < 0.5) {
        first = getRandomItem(maleNames);
        icon = '👨';
      } else {
        first = getRandomItem(femaleNames);
        icon = '👩';
      }
    }

    const last = getRandomItem(lastNames);
    const fullName = `${first} ${last}`.trim();
    currentGenerated.push(fullName);

    const li = document.createElement('li');
    li.className = 'name-item';
    li.innerHTML = `
      <span><span class="gender-icon">${icon}</span>${fullName}</span>
      <button class="copy-single-btn" title="Copy name" data-name="${fullName}">📋</button>
    `;

    li.querySelector('.copy-single-btn').addEventListener('click', (e) => {
      e.stopPropagation();
      copyToClipboard(fullName);
    });

    nameResultsList.appendChild(li);
  }

  state.lastGeneratedNames = currentGenerated;
}

/**
 * Batch Generate for All Wishlist Countries
 */
function generateBatchWishlist() {
  if (state.wishlist.length === 0) return;

  // Hide single generator
  generatorSection.style.display = 'none';
  batchResultsSection.style.display = 'block';
  batchResultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

  batchContainer.innerHTML = '';
  const allBatchNames = [];
  const count = state.nameCount || 5;
  const gender = state.activeGender;

  state.wishlist.forEach(countryItem => {
    const fullCountry = state.allCountries.find(c => c.code === countryItem.code) || countryItem;
    const poolKey = fullCountry.pool;
    const pool = DATA.pools[poolKey] || DATA.pools['anglo_western'];

    const maleNames = pool.male_first || [];
    const femaleNames = pool.female_first || [];
    const lastNames = pool.last_names || [];

    const countryNames = [];
    for (let i = 0; i < count; i++) {
      let first = '';
      let icon = '';
      if (gender === 'male') {
        first = getRandomItem(maleNames);
        icon = '👨';
      } else if (gender === 'female') {
        first = getRandomItem(femaleNames);
        icon = '👩';
      } else {
        if (Math.random() < 0.5) {
          first = getRandomItem(maleNames);
          icon = '👨';
        } else {
          first = getRandomItem(femaleNames);
          icon = '👩';
        }
      }
      const last = getRandomItem(lastNames);
      countryNames.push({ full: `${first} ${last}`.trim(), icon });
      allBatchNames.push(`[${countryItem.name}] ${first} ${last}`);
    }

    // Build block
    const block = document.createElement('div');
    block.className = 'batch-country-block';
    block.innerHTML = `
      <div class="batch-country-title">
        <span>${countryItem.flag} ${countryItem.name} (${count} টি নাম)</span>
        <button class="secondary-btn" style="padding:4px 10px; font-size:0.78rem;" data-copy="${countryItem.name}">📋 Copy Country Names</button>
      </div>
      <ul class="name-results-list">
        ${countryNames.map(n => `
          <li class="name-item">
            <span><span class="gender-icon">${n.icon}</span>${n.full}</span>
            <button class="copy-single-btn" data-name="${n.full}">📋</button>
          </li>
        `).join('')}
      </ul>
    `;

    // Copy country specific names
    block.querySelector('[data-copy]').addEventListener('click', () => {
      copyToClipboard(countryNames.map(n => n.full).join('\n'));
    });

    // Copy single items
    block.querySelectorAll('.copy-single-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        copyToClipboard(btn.getAttribute('data-name'));
      });
    });

    batchContainer.appendChild(block);
  });

  state.lastBatchNames = allBatchNames;
}

function getRandomItem(arr) {
  if (!arr || arr.length === 0) return 'Name';
  return arr[Math.floor(Math.random() * arr.length)];
}

/**
 * Copy to Clipboard
 */
function copyToClipboard(text) {
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(showCopyAlert);
  } else {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-999999px';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
      showCopyAlert();
    } catch (err) {
      console.error('Fallback copy failed', err);
    }
    document.body.removeChild(textArea);
  }
}

function showCopyAlert() {
  copyNotice.style.display = 'inline';
  setTimeout(() => {
    copyNotice.style.display = 'none';
  }, 2000);
}

/**
 * Event Listeners
 */
function setupEventListeners() {
  // Search
  countrySearch.addEventListener('input', (e) => {
    handleSearch(e.target.value);
  });

  clearSearchBtn.addEventListener('click', () => {
    countrySearch.value = '';
    handleSearch('');
    countrySearch.focus();
  });

  // Top view toggle buttons
  resetViewBtn.addEventListener('click', () => {
    countrySearch.value = '';
    clearSearchBtn.style.display = 'none';
    setFeaturedView();
  });

  allCountriesBtn.addEventListener('click', () => {
    countrySearch.value = '';
    clearSearchBtn.style.display = 'none';
    setAllCountriesView();
  });

  // Pagination buttons
  prevPageBtn.addEventListener('click', () => {
    if (state.currentPage > 1) {
      state.currentPage--;
      renderGrid();
    }
  });

  nextPageBtn.addEventListener('click', () => {
    const totalPages = Math.ceil(state.filteredCountries.length / PAGE_SIZE);
    if (state.currentPage < totalPages) {
      state.currentPage++;
      renderGrid();
    }
  });

  // Wishlist Toggle in Panel
  toggleWishlistBtn.addEventListener('click', () => {
    if (state.selectedCountry) {
      toggleWishlist(state.selectedCountry);
    }
  });

  // Batch Wishlist Order Button
  batchWishlistBtn.addEventListener('click', () => {
    generateBatchWishlist();
  });

  batchRegenBtn.addEventListener('click', () => {
    generateBatchWishlist();
  });

  copyAllBatchBtn.addEventListener('click', () => {
    if (state.lastBatchNames && state.lastBatchNames.length > 0) {
      copyToClipboard(state.lastBatchNames.join('\n'));
    }
  });

  closeBatchBtn.addEventListener('click', () => {
    batchResultsSection.style.display = 'none';
  });

  // Close generator panel
  closeGenBtn.addEventListener('click', () => {
    generatorSection.style.display = 'none';
    state.selectedCountry = null;
    renderGrid();
  });

  // Gender selection
  genderButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      genderButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      state.activeGender = btn.getAttribute('data-gender');
      saveStorage();
      if (generatorSection.style.display !== 'none') generateNames();
      if (batchResultsSection.style.display !== 'none') generateBatchWishlist();
    });
  });

  // Quantity preset buttons
  qtyButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      qtyButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      customQtyInput.value = '';
      state.nameCount = parseInt(btn.getAttribute('data-qty'), 10);
      saveStorage();
      if (generatorSection.style.display !== 'none') generateNames();
      if (batchResultsSection.style.display !== 'none') generateBatchWishlist();
    });
  });

  // Custom quantity input
  customQtyInput.addEventListener('input', (e) => {
    const val = parseInt(e.target.value, 10);
    if (!isNaN(val) && val >= 1 && val <= 100) {
      qtyButtons.forEach(b => b.classList.remove('active'));
      state.nameCount = val;
      saveStorage();
      if (generatorSection.style.display !== 'none') generateNames();
      if (batchResultsSection.style.display !== 'none') generateBatchWishlist();
    }
  });

  // Generate Button
  generateBtn.addEventListener('click', () => {
    generateNames();
  });

  // Copy All Button
  copyAllBtn.addEventListener('click', () => {
    if (state.lastGeneratedNames && state.lastGeneratedNames.length > 0) {
      const allText = state.lastGeneratedNames.join('\n');
      copyToClipboard(allText);
    }
  });
}

// Start
document.addEventListener('DOMContentLoaded', init);

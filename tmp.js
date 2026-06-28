(function () {
"use strict";

/**
 * @file settings.js
 * @description Surfingkeys settings options.
 *
 * This file defines values for existing settings from surfingkeys api.
 * It don`t create nothing new, only attributes values to the already existing settings element,
 * created on the original surfingkeys project.
 *
 * Each settings description and type may be found here on the section bellow, or the file README.
 *
 * The type definitions from this settings elements is done in types/project-globals.d.ts
 *
 * Any new addition here needs to be only an update from an existing settings in surfingkeys, and
 * should be also included in project-globals.d.ts
 */

/**
 * @typedef {Object} SurfingKeysSettings
 *
 * @property {boolean} autoSpeakOnInlineQuery
 *   Whether to automatically speak the query string with TTS on inline query.
 *   @default false
 *
 * @property {string} lastKeys
 *   Last executed key sequence.
 *
 * @property {boolean} smartCase
 *   Whether to make caseSensitive true if the search pattern contains upper case characters.
 *   @default true
 *
 * @property {boolean} caseSensitive
 *   Whether finding in page/Omnibar is case sensitive.
 *   @default false
 *
 * @property {RegExp} clickablePat
 *   A regex to detect clickable links from text, you could use `O` to open them.
 *   @default /(https?&#124;thunder&#124;magnet):\/\/\S+/ig
 *
 * @property {"left"|"right"|"center"} hintAlign
 *   Alignment of hints on their target elements.
 *   @default "center"
 *
 * @property {"default"|"left"|"right"|"first"|"last"} newTabPosition
 *   Where to new tab.
 *   @default "default"
 *
 * @property {number} omnibarMaxResults
 *   How many results will be listed out each page for Omnibar.
 *   @default 10
 *
 * @property {string[]} ignoredFrameHosts
 *   When using `w` to loop through frames, you could use this settings to exclude some of them, such as those for advertisements.
 *   @default ["https://tpc.googlesyndication.com"]
 *
 * @property {RegExp} blocklistPattern
 *   A regex to match the sites that will have Surfingkeys disabled.
 *   @default
 *
 * @property {RegExp} lurkingPattern
 *   User can specify the pages where Surfingkeys will lurk until it is called out by `Alt-i` or `p`(for ephemeral case)
 *   @default undefined
 *
 * @property {string} clickableSelector
 *   Extra CSS selector to pick elements for hints mode, such as "\*.jfk-button, \*.goog-flat-menu-button". |
 *   @default ""
 *
 * @property {string} editableSelector
 *   CSS selector for additional editable elements.
 *   @default "div.CodeMirror-scroll,div.ace_conten"
 *
 * @property {boolean} cursorAtEndOfInput
 *   Whether to put cursor at end of input when entering an input box, by false to put the cursor where it was when focus was removed from the input.
 *   @default true
 *
 * @property {boolean} digitForRepeat
 *   Whether digits are reserved for repeats, by false to enable mapping of numeric keys.
 *   @default true
 *
 * @property {boolean} cursorAtEndOfInput
 *   Whether digits are reserved for repeats, by false to enable mapping of numeric keys.
 *   @default true
 *
 * @property {string} defaultSearchEngine
 *  The default search engine used in Omnibar.
 *  @default "g"
 *
 * @property {boolean} editableBodyCare
 *   Insert mode is activated automatically when an editable element is focused, so if document.body is editable for some window/iframe (such as docs.google.com), Insert mode is always activated on the window/iframe, which means all shortcuts from Normal mode will not be available. With `editableBodyCare` as `true`, Insert mode will not be activated automatically in this case.
 *   @default true
 *
 * @property {boolean} enableAutoFocus
 *   Whether to enable auto focus after mouse click on some widget. This is different with `stealFocusOnLoad`, which is only for the time of page loaded. For example, there is a hidden input box on a page, it is turned to visible after user clicks on some other link. If you don't like the input to be focused when it's turned to visible, you could set this to false.
 *   @default true
 *
 * @property {boolean} enableEmojiInsertion
 *   Whether to turn on Emoji completion in Insert mode.
 *   @default false
 *
 * @property {boolean} focusFirstCandidate
 *   Whether to focus first candidate of matched result in Omnibar.
 *   @default false
 *
 * @property {boolean} focusOnSaved
 *   Whether to focus text input after quitting from vim editor.
 *   @default true
 *
 * @property {boolean} hintExplicit
 *   Whether to wait for explicit input when there is only a single hint available
 *   @default false
 *
 * @property {boolean} hintShiftNonActive
 *   Whether new tab is active after entering hint while holding shift
 *   @default false
 *
 * @property {boolean} historyMUOrder
 *   Whether to list history in order of most used beneath Omnibar.
 *   @default true
 *
 * @property {boolean} launguage
 *   The language of the usage popover
 *   @default undefined
 *
 * @property {""|"Caret"|"Normal"} modeAfterYank
 *   Which mode to fall back after yanking text in visual mode.
 *   @default ""
 *
 * @property {RegExp} nextLinkRegex
 *   A regex to match links that indicate next page.
 *   Include english, portuguese and chinese default notation.
 *   @default /(\bnext\b)|(\bmais\b)|(\bpnnext\b)|下页|下一页|后页|下頁|下一頁|後頁|>>|»/i;
 *
 * @property {RegExp} prevLinkRegex
 *   A regex to match links that indicate previous page.
 *   Include english, portuguese and chinese default notation.
 *   @default /(\bprev\b)|(\bprevious\b)|(\banterior\b)|(\bpnprev\b)|上页|上一页|前页|上頁|上一頁|前頁|<<|«/i;
 *
 * @property {number} repeatThreshold
 *   The maximum of actions to be repeated.
 *   @default 9
 *
 * @property {number} omnibarHistoryCacheSize
 *   The maximum of items fetched from browser history.
 *   @default 100
 *
 * @property {"middle"|"bottom"} omnibarPosition
 *   Where to position Omnibar.
 *   @default "middle"
 *
 * @property {boolean} omnibarSuggestion
 *   Show suggestion URLs
 *   @default false
 *
 * @property {number} omnibarSuggestionTimeout
 *   Timeout duration before Omnibar suggestion URLs are queried, in milliseconds. Helps prevent unnecessary HTTP requests and API rate-limiting.
 *   @default 200
 *
 * @property {number} richHintsForKeystroke
 *   Timeout(ms) to show rich hints for keystroke, 0 will disable rich hints.
 *   @default 500
 *
 * @property {number} scrollStepSize
 *   A step size for each move by `j`/`k`
 *   @default 70
 *
 * @property {boolean} showModeStatus
 *   Whether always to show mode status.
 *   @default false
 *
 * @property {boolean} showProxyInStatusBar
 *   Whether to show proxy info in status bar.
 *   @default false
 *
 * @property {boolean} smoothScroll
 *   Whether to use smooth scrolling when pressing keys like `j`/`k`/`e`/`d` to scroll page or elements.
 *   @default true
 *
 * @property {number} startToShowEmoji
 *   How many characters are needed after colon to show emoji suggestion.
 *   @default 2
 *
 * @property {boolean} stealFocusOnLoad
 *   Whether to prevent focus on input on page loaded, set to true by default so that we could use Surfingkeys directly after page loaded, otherwise we need press `Esc` to quit input.
 *   @default true
 *
 * @property {number} tabsThreshold
 *   When total of opened tabs exceeds the number, Omnibar will be used for choosing tabs.
 *   @default 100
 *
 * @property {boolean} verticalTabs
 *   Whether to show tab pickers vertically aligned.
 *   @default true
 *
 * @property {"left"|"right"|"last"} focusAfterClosed
 *   Which tab will be focused after the current tab is closed.
 *   @default "right"
 *
 * @property {number} scrollFriction
 *   A force that is needed to start continuous scrolling after initial scroll step. A bigger number will cause a flicker after initial step, but help to keep the first step precise.
 *   @default 0
 *
 * @property {string} aceKeyBindings
 *   Set it "emacs" to use emacs keybindings in the ACE editor.
 *   @default "vim"
 *
 * @property {[number, number, number, number]} caretViewport
 *   Set it in format `[top, left, bottom, right]` to limit hints generation on `v` for entering visual mode, such as `[window.innerHeight / 2 - 10, 0, window.innerHeight / 2 + 10, window.innerWidth]` will make Surfingkeys generate Hints only for text that display on vertically middle of window.
 *   @deaulf {}
 *
 * @property {object} mouseSelectToQuery
 *   All hosts that have enable feature -- mouse selection to query.
 *   @default //
 *
 * @property {boolean} useLocalMarkdownAPI
 *   Whether to use [chjj/marked](https://github.com/chjj/marked) to parse markdown, otherwise use github markdown API.
 *   @default true
 *
 * @property {string} disabledOnActiveElementPattern
 *   Automatically disable this extension when the active element matches with this pattern and reactivate the extension when the active element changes, one useful case is to enable user to type to locate an option in a large dropdown, such as `settings.disabledOnActiveElementPattern = "ul.select-dropdown-options";`
 *   @default ""
 *
 * @property {boolean} scrollFallback
 *   Fallback to document-level scrolling when the focused element cannot scroll in the requested direction.
 *   @default false
 *
 * @property {RegExp} textAnchorPat
 *  Pattern to identify text anchor elements.
 *
 * @property {"bedrock" | "gemini" | "ollama" | "deepseek" | "custom"} defaultLLMProvider
 *   LLM type to be used.
 *
 * @property {boolean} useNeovim
 *   the vim editor will be the embeded JS implementation, if `useNeovim` is true, neovim will
 *   be used through natvie messaging.
 *   By time, only browsers based on chrome includes the possibility of this implementation.
 *   @default false
 *
 * @propery {llm}
 */

api.Hints.setCharacters("asdfghlzxcvbnmqwertyuiop");
settings.autoSpeakOnInlineQuery = false;
settings.lastKeys = "";
settings.blocklistPattern = "";
settings.lurkingPattern = "";
settings.disabledOnActiveElementPattern = "";
settings.smartCase = true;
settings.caseSensitive = false;
settings.clickablePat = /(https?:\/\/|thunder:\/\/|magnet:)\S+/gi;
settings.clickableSelector = "";
settings.editableSelector = "div.CodeMirror-scroll,div.ace_content";
settings.cursorAtEndOfInput = true;
settings.defaultLLMProvider = "ollama";
settings.defaultSearchEngine = "g";
settings.defaultVoice = "Daniel";
settings.editableBodyCare = true;
settings.enableAutoFocus = true;
settings.enableEmojiInsertion = false;
settings.experiment = true;
settings.focusFirstCandidate = false;
settings.focusOnSaved = true;
settings.hintAlign = "left";
settings.hintExplicit = false;
settings.hintShiftNonActive = false;
settings.historyMUOrder = true;
settings.lastQuery = "";
settings.modeAfterYank = "";
settings.nextLinkRegex =
  /(\bnext|pnnext|próximo|seguinte\b)|下页|下一页|后页|下頁|下一頁|後頁|>>|»/i;
settings.digitForRepeat = true;
settings.omnibarMaxResults = 20;
settings.omnibarHistoryCacheSize = 200;
settings.omnibarPosition = "middle";
settings.omnibarSuggestion = true;
settings.omnibarSuggestionTimeout = 300;
settings.omnibarTabsQuery = {};
settings.pageUrlRegex = "";
settings.prevLinkRegex =
  /(\bprev|previous|pnprev|anterior\b)|上页|上一页|前页|上頁|上一頁|前頁|<<|«/i;
settings.newTabPosition = "default";
settings.repeatThreshold = 9;
settings.richHintsForKeystroke = 1000;
settings.scrollFallback = false;
settings.scrollStepSize = 80;
settings.showModeStatus = true;
settings.showProxyInStatusBar = false;
settings.smartPageBoundary = false;
settings.smoothScroll = true;
settings.startToShowEmoji = 2;
settings.stealFocusOnLoad = true;
settings.tabIndicesSeparator = "|";
settings.tabsThreshold = 100;
settings.verticalTabs = true;
//settings.textAnchorPat = /(^[\n\r\s]*\S{3,}|\b\S{4,})/g;
settings.ignoredFrameHosts = ["https://tpc.googlesyndication.com"];
settings.scrollFriction = 0;
settings.aceKeybindings = "vim";
settings.caretViewport = {};
settings.mouseSelectToQuery = [
  "http://localhost",
  "https://localhost",
  "http://127.0.0.1",
  "https://127.0.0.1",
];
settings.useNeovim = false;
settings.useLocalMarkdownAPI = true;
//settings.llm = {
//custom: {
//serviceUrl: "https://api.openai.com/v1/chat/completions",
//apiKey: "sk-proj-...",
//model: "gpt-5.4",
//}
//};
//settings.language = "";
//settings.focusAfterClosed = "right";


/**
 * @file utils.js
 * @description Provides general utility functions for the SurfingKeys extension.
 *
 * Surfingkeys personal module utils functions.
 *
 * This file defines:
 *
 * Hints elements groups
 * ---------------------
 *  {string}
 * `utils.mainHints`, `utils.buttonHints`, `utils.fullScreenHints`, `utils.videoHints`,
 * `utils.thumbHint`, `utils.defaultSelector`
 *
 * Mouse events
 * ------------
 *  {MouseEvent}
 *  `utils.mouseOver`, `utils.mouseVideo`, `utils.mouseDown`
 *  MOUSE_EVENTS = ['mouseover', 'pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click', 'focus', 'focusin'];
 *
 *
 * Categories groups
 * -----------------
 * {object}
 * `utils.categories`
 *
 * Basics main functions
 * ---------------------
 * `utils.createHints`,
 *
 * Configuration writing/loading functions
 * =======================================
 *
 * Keymaps registering
 * -------------------
 * `utils.registerShortcuts`, `utils.registerAltShortcuts`, `utils.registerSearchEngines`,
 * `utils.loadUnmaps`
 *
 * Themes / Color schemes
 * ----------------------
 * `utils.loadVisualTheme`, `utils.loadHintsTheme`, `utils.loadColorScheme`
 *
 * Creating new functions helpers
 * ------------------------------
 * `utils.findClosestEl`, `utils.findClosestToUser`
 *
 * Scrolling utils
 * ---------------
 * `utils.hasScroll`, `utils.scrollableMousedownHandler`, `utils.getScrollableElements`,
 * `utils.initScrollIndex`, `utils.refreshScrollableElements`, `utils.resetScrollTarget`,
 * `utils.focusScrollTarget`
 *
 * Surfkingkeys api implementations
 * --------------------------------
 *`utils.dispatchSKEvent`, `utils.highlightElement`
 */

const utils = {};

/** CSS elements hints lists/strings. Used on creating hintings of elements, and by some other
 * functions that use specific elements actions.
 */

/** @type {HTMLElement[] | number | null} */
let scrollNodes,
  scrollIndex = 0;

/**
 * Main surfingkeys hinting generating elements group list.
 *
 * @kind object
 * @name utils.mainHints
 */
utils.mainHints = [
  ".btn",
  "[href]",
  "[src]",
  "a[href]",
  "button",
  "*",
  "a[video]",
  "a[player]",
  "a[media]",
  "onclick",
  "checkbox",
].join(",");

/**
 * Buttons type elements hints
 *
 * @kind {string} buttonHints
 * @name utils.buttonHints
 */
utils.buttonHints = [".button", ".btn", ".vjs-button-icon", ".vjs-big-play-button", "button"].join(
  ","
);

/**
 * Fullscreen buttons type elements hints
 *
 * @kind object
 * @name utils.fullScreenHints
 */
utils.fullScreenHints = [
  "vjs-fullscreen-control",
  "vjs-control",
  "vjs-button",
  ".Full screen",
  ".Fullscreen",
  ".fullScreen",
].join(",");

/**
 * Code blocks copy button hints
 *
 * @kind object
 * @name utils.codeBlockHints
 */
utils.codeBlockHints = [
  "[aria-label='Copy']",
  "[aria-label='copy']",
  ".CopyButton",
  "button.copybtn",
  "[data-tooltip='Copy']",
  '[id^="codecell"]',
  '[id^="copy-button"]',
  ".icon-tabler-copy",
  "[title='Copy']",
  ".copy-icon",
].join(",");

/**
 * Video type elements hints
 *
 * @kind object
 * @name utils.videoHints
 */
utils.videoHints = [
  "video",
  ".video",
  "player",
  ".player",
  "player-video",
  ".player-video",
  "video-player",
  ".video-player",
  ".vjs-tech",
  "shreddit-player-2",
  "vjs-tech",
  "video.vjs-tech",
  "thumbnail",
  ".thumbnail",
].join(",");

utils.linkHints = [
  /* link-like */
  "a[href]",
  "area[href]",
  "link[href]",
  "*[href]",
  ".href",
  /* media-like */
  "img[src], img[srcset]",
  "video[src]",
  "audio[src]",
  "source[src]",
  "track[src]",
  "iframe[src]",
  "embed[src]",
  "script[src]",
  "*[src]",
  "[data-src]",
  "[data-href]",
  "[data-url]",
  /* button-like */
  "button",
  ".btn",
  "btn",
  ".button",
  "[role='button']",
].join(",");

//CHECK: Check if possible to remove or if needed to implement thumbnail hints

/**
 * Thumbnails type elements hints
 *
 * @kind string
 * @name utils.thumbHint
 */
utils.thumbHint = ["img"].join(",");

/**
 * Default hint elements selector
 *
 * @kind string
 * @name utils.defaultSelector
 */
utils.defaultSelector = "a[href]:not([href^=javascript])";

/**
 * Input hint elements selector
 *
 * @kind string
 * @name utils.inputHint
 */
utils.inputHints = [
  "input:not([type=submit])",
  "textarea",
  "*[contenteditable=true]",
  "*[role=textbox]",
  "select",
  "div.ace_cursor",
].join(",");

/**
 * Mouse event to hover over placing the mouse on given element.
 *
 * @kind MouseEvent
 * @see commands.mouseOver
 */
const mouseOver = new MouseEvent("mouseover", {
  bubbles: false,
  cancelable: true,
});

utils.mouseOver = mouseOver;

const mouseLeft = new MouseEvent("click", {
  bubbles: true,
  cancelable: true,
  button: 0,
  buttons: 1,
  //view: window,
});

utils.mouseLeft = mouseLeft;

const mouseEnter = new MouseEvent("mouseenter", {
  bubbles: true,
  cancelable: true,
});

utils.mouseEnter = mouseEnter;

const mouseMove = new MouseEvent("mousemove", {
  bubbles: true,
  cancelable: true,
});

/**
 * Check if passed element is currently visible.
 * @param {HTMLElement} elm
 * @return {boolean}
 */
utils.isElementVisible = (elm) => {
  return elm.offsetHeight > 0 && elm.offsetWidth > 0;
};

/**
 * Check if passed element is possible to be clicked.
 * @param {HTMLElement} e
 * @return {boolean}
 */
utils.isElementClickable = (e) => {
  let cssSelector =
    "a, button, select, input, textarea, summary, *[onclick], *[contenteditable=true], *.jfk-button, *.goog-flat-menu-button, *[role=button], *[role=link], *[role=menuitem], *[role=option], *[role=switch], *[role=tab], *[role=checkbox], *[role=combobox], *[role=menuitemcheckbox], *[role=menuitemradio]";
  //if (settings.clickableSelector.length) {
    //cssSelector += ", " + settings.clickableSelector;
  //}

  return (
    e.matches(cssSelector) ||
    getComputedStyle(e).cursor === "pointer" ||
    getComputedStyle(e).cursor.slice(0, 4) === "url(" ||
    e.closest("a, *[onclick], *[contenteditable=true], *.jfk-button, *.goog-flat-menu-button") !==
      null
  );
};

/**
 * Escape text for safe HTML insertion.
 *
 * @param {string} text - Text to escape.
 * @returns {string} Escaped HTML string.
 */
utils.escapeHTML = (text) => {
  const el = document.createElement("a");
  el.textContent = text;
  return el.innerHTML;
};

/**
 * @typedef {Object.<string, unknown> & { url?: string }} SuggestionItemProps
 */

/**
 * @typedef {object} SuggestionItem
 * @property {string} html - Rendered HTML for the suggestion item.
 * @property {SuggestionItemProps} props - Extra metadata associated with the item.
 */

/**
 * Create a suggestion item from HTML and optional props.
 *
 * @param {string} html - HTML content for the item.
 * @param {SuggestionItemProps} [props={}] - Extra properties for the item.
 * @returns {SuggestionItem} Suggestion item object.
 */
utils.createSuggestionItem = (html, props = {}) => {
  const li = document.createElement("li");
  li.innerHTML = html;
  return { html: li.outerHTML, props };
};

/**
 * Create a suggestion item representing a URL entry.
 *
 * @param {string} title - Display title for the URL.
 * @param {string} url - URL string.
 * @param {boolean} [sanitize=true] - Whether to sanitize the values.
 * @returns {SuggestionItem} Suggestion item object.
 */
utils.createURLItem = (title, url, sanitize = true) => {
  let t = title;
  let u = url;
  if (sanitize) {
    t = utils.escapeHTML(t);
    u = new URL(u).toString();
  }
  return utils.createSuggestionItem(
    `
      <div class="title">${t}</div>
      <div class="url">${u}</div>
    `,
    { url: u }
  );
};

utils.mouseMove = mouseMove;
/**
 * Mouse event to click on video elements.
 *
 * @kind MouseEvent
 * @see commands.toggleMuteVideo
 * @see commands.togglePlayVideo
 */
const mouseVideo = new MouseEvent("mouseover", {
  bubbles: true,
  cancelable: true,
});

utils.mouseVideo = mouseVideo;

/**
 * Mouse down event, to focus scrollable elements for example.
 *
 * @kind MouseEvent
 */
const mouseDown = new MouseEvent("mousedown", {
  bubbles: false,
  cancelable: true,
});

utils.mouseDown = mouseDown;

const mouseClick = new MouseEvent("click", {
  bubbles: true,
  cancelable: true,
  composed: true,
});
utils.mouseClick = mouseClick;

const mouseHold = new MouseEvent("click", {
  bubbles: false,
  cancelable: true,
  composed: true,
});
utils.mouseHold = mouseHold;

/**
 * Categories groups used in `mapkeys` shortcuts definitions groups.
 *
 * @name utils.categories
 * @kind object
 * @see {string}
 */
utils.categories = {
  help: 0,
  mouseClick: 1,
  scroll: 2,
  tabs: 3,
  pageNav: 4,
  sessions: 5,
  searchSelectedWith: 6,
  clipboard: 7,
  omnibar: 8,
  visualMode: 9,
  vimMarks: 10,
  settings: 11,
  chromeURLs: 12,
  proxy: 13,
  misc: 14,
  insertMode: 15,
};

// -TODO: Check better working version of function
/**
 * A constructable DOM Event class (e.g., Event, MouseEvent, KeyboardEvent, InputEvent).
 *
 * @template {Event} TEvent
 * @typedef {new (type: string, eventInitDict?: any) => TEvent} DomEventConstructor
 */

/**
 * Dispatch one or more DOM events on a given node.
 *
 * @param {DomEventConstructor<Event>} EventCtor
 *     Event constructor (Event, MouseEvent, KeyboardEvent, etc.).
 * @param {EventTarget} node
 *     Target that will receive the events.
 * @param {...string} eventTypes
 *     One or more event type names.
 *
 * @example
 * utils.dispatchEvents(MouseEvent, element, "mousedown", "mouseup", "click");
 * utils.dispatchEvents(KeyboardEvent, window, "keydown", "keyup");
 */
utils.dispatchEvents = (
  /** @type {DomEventConstructor<Event>} */ EventCtor,
  /** @type {EventTarget} */ node,
  ...eventTypes
) => {
  for (const type of eventTypes) {
    /** @type {Event} */
    const ev = new EventCtor(type, {
      bubbles: true,
      cancelable: true,
    });

    node.dispatchEvent(ev);
  }
};

/**
 * Open the Ace editor and resolve with entered text.
 *
 * @returns {Promise<string>}
 */
utils.getEditorInput = () => {
  return new Promise((resolve) => {
    api.Front.showEditor("", (runinput) => {
      resolve(runinput);
    });
  });
};

/**
 * Create hints and run `action` with the chosen element.
 *
 * @template {HTMLElement} T
 * @param {string | readonly T[] | null} [selector=utils.defaultSelector]
 * @param {(element: T, event?: Event) => void} [action=api.Hints.dispatchMouseClick]
 * @param {object} [attrs]
 * @returns {Promise<number>}
 */
utils.createHints = (
  selector = utils.defaultSelector,
  action = api.Hints.dispatchMouseClick,
  attrs = {}
) => {
  return api.Hints.create(
    selector,
    (element, event) => {
      action(element, event);
    },
    attrs
  );
};
/**
 * Registers all shortcuts with SurfingKeys.
 *
 * Notes that site specific shortcuts are urrently executed before the site specific unmaps, in
 * this way unmapping used shortcuts without leader don't needing to be includded in site unmaps.
 *
 * @description The `shortcuts` mappings object is defined in `shortcuts.js`, and accepts two
 * possible formattings:
 *
 * @param {string} siteSpecificLeader
 */
utils.registerShortcuts = (siteSpecificLeader) => {
  // Register global shortcuts

  shortcuts.global.forEach((s) => {
    api.unmap(s.key);
  });

  shortcuts.global.forEach(({ key, command, category, description }) => {
    /** @type {Record<string, number>} */
    const categories = utils.categories;
    const categoryKey = category ?? "misc";
    const categoryGroup = `#${categories[categoryKey] ?? 14}`;
    api.mapkey(key, `${categoryGroup} ${description}`, command);
  });

  // Register domain-specific shortcuts

  shortcuts.sites.forEach(({ domain, mappings }) => {
    mappings.forEach(({ key, command, category, description, leader }) => {
      /** @type {Record<string, number>} */
      const categories = utils.categories;
      const categoryKey = category ?? "misc";
      const categoryGroup = `#${categories[categoryKey] ?? 14}`;
      const shortcutLeader = leader === false ? "" : siteSpecificLeader;
      api.mapkey(`${shortcutLeader}${key}`, `${categoryGroup} ${description}`, command, {
        domain,
      });
    });
  });
  console.log("✅ Normal mode SurfingKeys shortcuts registered.");
};

utils.registerNewCommands = () => {
  shortcuts.commands.forEach((cmd) => {
    utils.dispatchSKEvent("front", ["addCommand", cmd.name, cmd.desc, cmd.action]);
  });
  console.log("✅ New commands registered.");
};

/**
 * Registers other than the main shortcuts on SurfingKeys.
 *
 * @interface
 * @name utils.registerShortcuts
 */
utils.registerAltShortcuts = () => {
  // Register command mode omnibar shortcuts
  command_shortcuts.mappings.forEach((shct) => {
    api.unmap(shct.map);
    api.cmap(shct.alias, shct.map, null, shct.annot);
  });

  // Register aced text editor shortcuts
  acemaps.mappings.forEach((shct) => {
    const nmode = shct.mode || "normal";
    api.aceVimMap(shct.alias, shct.map, nmode);
  });
  console.log("✅ Ace editor and command omnibar mode SurfingKeys shortcuts registered.");
};

/**
 * Load user setted visual theme color scheme.
 *
 * To configure theme to be used, edit `sk.config.json` options.
 *
 * @param {string} themeName?
 * @name utils.loadVisualTheme
 */
utils.loadVisualTheme = (themeName) => {
  const currentTheme = theme.visual[themeName] || theme.visual.du;
  currentTheme.forEach((vtheme) => {
    api.Visual.style(
      `${vtheme.type}`,
      `
      background-color: ${vtheme.background_color};
      color: ${vtheme.color};`
    );
  });
};

/**
 * registerSearchEngines
 *
 * Read `searchEngines.mappings` from `scripts/server.js`, with each element of it being the
 * definition of a search engine.
 *
 * @param {string} searchLeader searchLeader key, readed from `sk.config.json`
 *
 * @see sk.config.json
 * @see scripts/search-engines.js
 *
 * Before creating the search engine, the function remove any existing search engine with similar
 * alias and if the alias matches more then one char (like "go"), it also remove any search engine
 * with only the first character of it (in this case, a search engine matching "g").
 *
 * Each search engine element will define the following commands and shortcuts keys:
 *
 * - Search in a new tab - `searchEngineLeader` + `alias`
 *   Search with the current search engine and open the result in a new tab, binding to the search
 *   engine leader key defined in `sk.config.json` + the current search engine alias element.
 *
 * - Search clipboard content - `searchClipboardLeader` + `alias`
 *   Search the current clipboard content with the search engine, binding to the search clipboard
 *   leader defined in `sk.config.json` + the curent search engine alias element
 *
 * - Search selected with - `searchSelectedLeader` + `alias`
 *   Search current selection in normal or visual mode, with the search engine, binding to search
 *   selected leader defined in `sk.config.json` + the current search engine alias element
 *
 * - Search selected with interactive - `searchSelectedLeader.toUpperCase()` + `alias`
 *   Search current selection in normal or visual mode interacivelly, with the search engine,
 *   binding to search selected leader upercased + the current search engine alias element
 *
 *
 *
 * `api.addSearchAlias`
 *
 * Each search engine will be added to surfingkeys as an search alias by `api.addSearchAlias`, that
 * takes the parrameters:
 *
 *   - `Shortcut keys` : string
 *
 *   - `Alias name` : string
 *
 *   - `Search url` : string
 *
 *   - `Search leader key` : string - defined in `sk.config.json`
 *
 *   - `Suggestion url` : string - URL to fetch suggestions in omnibar when this search engine is
 *   triggered. (optional, default `null`)
 *
 *   - `Only this site key` : string - `<search_leader_key><only_this_site_key><alias>` in normal mode
 *   will search selected text within current site with this search engine directly without opening
 *   the omnibar, for example `aod`. (optional, default `o`)
 *
 *   - `options` : object `- favicon_url` URL for favicon for this search engine, `skipMaps` if
 *   `true` disable creating key mappings for this search engine (optional, default `null`)
 *
 *
 * `api.searchSelectedWith`
 *
 *  Search selected with to each search engine will be created by `api.searchSelectedWith`, that
 *  takes the parameters:
 *
 *   - `se` : string - a search engine's search URL
 *
 *   - `onlyThisSite` : boolean - whether to search only within current site, need support from the provided search engine. (optional, default `false`)
 *
 *   - `interactive` : boolean - whether to search in interactive mode, in case that you need some small modification on the selected content. (optional, default `false`)
 *
 *   - `alias` : string - only used with interactive mode, in such case the url from `se` is ignored, SurfingKeys will construct search URL from the alias registered by `addSearchAlias`. (optional, default `""`)

 *
 *
 * `api.mapkey`
 *
 * Each search shortcut is created by `api.mapkey` surfingkeys function.
 *
 *  The following shortcuts will be created:
 *
 *   - Shortcut to search in new tab
 *
 *   - Shortcut to search in current tab
 *
 *   - Shortcut to search clipboard content
 *
 */

/**
 * Check whether a URL is reachable.
 *
 * Uses a lightweight HEAD request when possible and falls back to
 * a simple fetch attempt for restricted environments.
 *
 * @param {string} url
 *   Absolute URL to be tested.
 *
 * @returns {Promise<boolean>}
 *   Resolves to true if the URL appears accessible.
 */
utils.urlExists = async (url) => {
  if (typeof url !== "string" || url.length === 0) {
    return false;
  }

  try {
    const response = await fetch(url, { method: "HEAD" });
    return response.ok;
  } catch {
    try {
      await fetch(url, { method: "GET", mode: "no-cors" });
      return true;
    } catch {
      return false;
    }
  }
};

/**
 *
 * Register search engines
 *
 * @param {string} searchLeader
 * @param {string} searchClipboardLeader
 * @param {string} searchSelectedLeader
 *
 * @returns {Promise<void>}
 *
 */
utils.registerSearchEngines = async (searchLeader, searchClipboardLeader, searchSelectedLeader) => {
  /** @type {string[]} */
  const removedAlias = [];

  const DEFAULT_FAVICON = "http://localhost:9334/favicons/search.ico";

  Object.values(searchEngines.mappings).forEach(async (s) => {
    const favicon_url = s.fav_icon || DEFAULT_FAVICON || null;

    /* 1. Try s.fav_icon if provided */
    //if (s.fav_icon && (await utils.urlExists(s.fav_icon))) {
    //favicon_url = s.fav_icon;

    /* 2. Otherwise try the default URL */
    //} else if (await utils.urlExists(DEFAULT_FAVICON)) {
    //favicon_url = DEFAULT_FAVICON;
    //}

    /*----------------------
    Search Engines Options
    ----------------------*/
    const options = {
      favicon_url,
      skipMaps: true,
    };

    /*---------------------------------------
    Removing search alias if already exists
    ---------------------------------------*/
    if (s.alias.length >= 2) {
      const oneCharAlias = s.alias.charAt(0);
      if (!removedAlias.includes(oneCharAlias)) {
        api.removeSearchAlias(oneCharAlias);
        removedAlias.push(oneCharAlias);
      }
    }

    if (!removedAlias.includes(s.alias)) {
      api.removeSearchAlias(s.alias);
      removedAlias.push(s.alias);
    }

    /*-------------------
    Adding Search Alias
    -------------------*/
    api.addSearchAlias(
      s.alias,
      s.name,
      s.search,
      searchLeader,
      s.compl,
      s.callback,
      undefined,
      options
    );

    /*------------------------------
    Adding Search Shortcut New Tab
    ------------------------------*/
    api.mapkey(`${searchLeader}${s.alias}`, `#8Search ${s.name}`, () =>
      api.Front.openOmnibar({ type: "SearchEngine", extra: s.alias, tabbed: true })
    );

    /*-------------------------------
    Adding Search Clipboard Content
    -------------------------------*/
    api.mapkey(
      `${searchClipboardLeader}${s.alias}`,
      `#7Search ${s.name} with clipboard contents`,
      () => {
        api.Clipboard.read((c) => {
          api.Front.openOmnibar({
            type: "SearchEngine",
            pref: c.data,
            extra: s.alias,
          });
        });
      }
    );

    /*---------------------------
    Adding Search Selected With
    --------------------------*/
    api.mapkey(
      `${searchSelectedLeader}${s.alias}`,
      `#6Interactive search selected with ${s.name}`,
      () => {
        api.searchSelectedWith(s.search, false, false);
      }
    );
    api.vmapkey(
      `${searchSelectedLeader}${s.alias}`,
      `#6Interactive search selected with ${s.name}`,
      () => {
        api.searchSelectedWith(s.search, false, false);
      }
    );

    /*---------------------------------------
    Adding Interactive Search Selected With
    ---------------------------------------*/
    api.mapkey(
      `${searchSelectedLeader.toUpperCase()}${s.alias}`,
      `#6Search selected with ${s.name}`,
      () => {
        api.searchSelectedWith(s.search, false, true, `${s.alias}`);
      }
    );
    api.vmapkey(
      `${searchSelectedLeader.toUpperCase()}${s.alias}`,
      `#6Search selected with ${s.name}`,
      () => {
        api.searchSelectedWith(s.search, false, true, `${s.alias}`);
      }
    );
  });
};

/**
 * Parse a size parameter into numeric value and unit.
 *
 * @param {string | number | null | undefined} input
 *     Size input (number/"N"/"Npx"/"Npt").
 *
 * @returns {{ value: number, unit: "px" | "pt" }}
 *     Parsed numeric value and unit.
 *
 * @throws {TypeError}
 *     If the input is not a valid size.
 */
utils.parseSizeParam = (input) => {
  /** @type {string} */
  const raw = String(input ?? "").trim();

  if (!raw) {
    throw new TypeError(`Invalid size value: "${input}"`);
  }

  /** @type {RegExpMatchArray | null} */
  const match = raw.match(/^(-?\d+(?:\.\d+)?)(px|pt)?$/i);

  if (match === null) {
    throw new TypeError(`Invalid size value: "${input}". Expected number, "Npx" or "Npt".`);
  }

  /** @type {number} */
  const value = Number(match[1]);

  if (!Number.isFinite(value)) {
    throw new TypeError(`Invalid numeric value: "${match[1]}"`);
  }

  /** @type {"px" | "pt"} */
  const unit = match[2] ? /** @type {"px" | "pt"} */ (match[2].toLowerCase()) : "px";

  return { value, unit };
};

/**
 * Load and apply a SurfingKeys hints theme with optional font sizes.
 *
 * The theme is read from `theme.hints[themeName]` falling back to `theme.hints.du`.
 * Font sizes accept:
 * - number (defaults to px)
 * - "Npx"
 * - "Npt"
 *
 * @param {string} themeName
 *     Theme key name to load from `theme.hints`.
 * @param {string | number | null | undefined} [fsHintsMain]
 *     Font size for "main" hint markers. Defaults to "15px".
 * @param {string | number | null | undefined} [fsHintsText]
 *     Font size for "text" hints. Defaults to "13px".
 *
 * @returns {void}
 *     This function returns nothing.
 */
utils.loadHintsTheme = (themeName, fsHintsMain, fsHintsText) => {
  /** @type {unknown} */
  const maybeTheme = theme?.hints?.[String(themeName)];

  /** @type {any[]} */
  const currentTheme = Array.isArray(maybeTheme) ? maybeTheme : theme?.hints?.du || [];

  /** @type {{ value: number, unit: "px" | "pt" }} */
  const mainSize = utils.parseSizeParam(fsHintsMain ?? "15px");

  /** @type {{ value: number, unit: "px" | "pt" }} */
  const textSize = utils.parseSizeParam(fsHintsText ?? "13px");

  /** @type {string} */
  const fsMainCss = `${mainSize.value}${mainSize.unit}`;

  /** @type {string} */
  const fsTextCss = `${textSize.value}${textSize.unit}`;

  /** @type {string} */
  const borderMain = `${mainSize.value / 5}${mainSize.unit}`;

  /** @type {string} */
  const borderText = `${textSize.value / 4}${textSize.unit}`;

  /** @type {string} */
  const defaultFontFamily = "'Source Code Pro', Ubuntu, sans-serif";

  for (const hint of currentTheme) {
    /** @type {string} */
    const type = String(hint?.type || "");

    /** @type {string} */
    const borderColor = String(hint?.border_color ?? hint?.background_color ?? "none");

    /** @type {string} */
    const color = String(hint?.color ?? "none");

    /** @type {string} */
    const background = String(hint?.background ?? "none");

    /** @type {string} */
    const backgroundColor = String(hint?.background_color ?? "none");

    /** @type {string} */
    const fontFamily = String(hint?.font_family ?? defaultFontFamily);

    if (type === "main") {
      api.Hints.style(
        [
          `border: solid ${borderMain} ${borderColor};`,
          `color: ${color};`,
          `background: ${background};`,
          `background-color: ${backgroundColor};`,
          `font-size: ${fsMainCss};`,
          `font-family: ${fontFamily};`,
        ].join("\n")
      );
      continue;
    }

    if (type === "text") {
      /** @type {string} */
      const beginColor = String(hint?.begin_color ?? hint?.color ?? "none");

      /** @type {string} */
      const beginBackgroundColor = String(
        hint?.begin_background_color ?? hint?.background_color ?? "none"
      );

      api.Hints.style(
        [
          `div{`,
          `  border: solid ${borderText} ${borderColor};`,
          `  color: ${color};`,
          `  background: ${background};`,
          `  background-color: ${backgroundColor};`,
          `  font-size: ${fsTextCss};`,
          `  font-family: ${fontFamily};`,
          `}`,
          `div.begin{`,
          `  color: ${beginColor};`,
          `  background-color: ${beginBackgroundColor};`,
          `}`,
        ].join("\n"),
        "text"
      );
    }
  }
};

/**
 * Inject on surfingkeys server text the loading lines to color scheme theme.
 *
 * @param {string} colorScheme
 * @param {string | number} fsGeneral
 * @param {string | number} fsBanner
 */
utils.loadColorScheme = (colorScheme, fsGeneral, fsBanner) => {
  fsGeneral = fsGeneral || 12;
  fsBanner = fsBanner || "18px";
  const cScheme = theme.colorSchemes[colorScheme];

  const lines = cScheme.split("\n");
  lines.splice(3, 0, `  --font-size: ${fsGeneral};`, `  --banner-font-size: ${fsBanner};`);
  const rootConfig = lines.join("\n");
  settings.theme = `
  ${rootConfig}

  ${theme.generic}
  `;
};

/**
 * Load unmapping of already defined keymaps commands.
 *
 * Also responsible for handling conflicts between global and site-specific matching keymaps.
 *
 * @name utils.loadUnmaps
 * @returns {void}
 */
utils.loadUnmaps = () => {
  const mappings = unmaps.mappings || [];

  for (const u of mappings) {
    /** @type {string[]} */
    const keys = typeof u.keys === "string" ? [u.keys] : u.keys;

    if (u.site === "global") {
      keys.forEach(
        /**
         * @param {string} k
         * @returns {void}
         */
        (k) => {
          api.unmap(k);
        }
      );
      continue;
    }

    /** @type {RegExp} */
    const regex = new RegExp(String(u.site));

    keys.forEach(
      /**
       * @param {string} k
       * @returns {void}
       */
      (k) => {
        api.unmap(k, regex);
      }
    );
  }
};

/**
 * Filter a node list by testing selected node fields against regular expressions.
 *
 * This version resets the regex state before each test, which is useful when
 * the provided expressions use the `g` or `y` flags.
 *
 * @param {Iterable<Node>} nodes - Nodes to filter.
 * @param {Object.<string, RegExp|string>} matchers - Property-to-regex mapping.
 * @returns {Node[]} Filtered nodes.
 *
 * @example
 * utils.filterNodesByFieldsSafe(document.querySelectorAll("button"), {"aria-controls": /(uid_\d)/i})
 */
utils.filterNodesByFieldsSafe = (nodes, matchers) => {
  return Array.from(nodes).filter((node) => {
    return Object.entries(matchers).every(([field, regex]) => {
      const regexp = regex instanceof RegExp ? regex : RegExp(regex);
      // @ts-ignore
      const value = node.getAttribute(field) || node[field];
      //console.log(`field: ${field}\nregexp: ${regex}\nvalue: ${value}`);
      //@return {{ x: number, y: number }}
      if (value === null) {
        return false;
      }
      regexp.lastIndex = 0;
      return regexp.test(String(value));
    });
  });
};

/**
 * Return page elements, optionally filtered by field-to-regexp matchers.
 *
 * When `matchers` is null, undefined, or empty, all document elements are
 * returned without filtering.
 *
 * @param {string} [nodeSelector="*"]
 * @param {Object.<string, RegExp> | null | undefined} [matchers=null]
 *   property-to-regexp mapping.
 * @returns {Node[]} Matching document elements.
 *
 * @example
 * const all = getDocumentElements();
 *
 * @example
 * const focusNodes = getDocumentElements({
 *   localName: /^(focus-)\w+$/i,
 * });
 */
utils.getDocumentElements = (nodeSelector = "*", matchers = null) => {
  const elements = Array.from(document.querySelectorAll(nodeSelector));

  if (matchers === null || Object.keys(matchers).length === 0) {
    return elements;
  }

  return elements.filter((element) => {
    return Object.entries(matchers).every(([field, regex]) => {
      if (!(regex instanceof RegExp)) {
        return false;
      }

      // @ts-ignore
      const value = element[field];
      if (value === null) {
        return false;
      }

      regex.lastIndex = 0;
      return regex.test(String(value));
    });
  });
};

/**
 * Find the closest element (by vertical distance) of a given selector
 * relative to the current viewport center.
 *
 * @param {string} selector
 *     CSS selector used to query elements.
 *
 * @returns {Element|HTMLElement|HTMLVideoElement|Node|null}
 *     Closest element to the viewport center, or null if none found.
 *
 * @example
 * const closestPost = utils.findClosestEl("shreddit-post");
 */
utils.findClosestEl = (selector) => {
  /** @type {NodeListOf<HTMLElement>} */
  const elements = document.querySelectorAll(selector);

  if (elements.length === 0) {
    return null;
  }

  /** @type {number} */
  const viewportCenter = window.innerHeight / 2;

  return Array.from(elements).reduce(
    /**
     * @param {HTMLElement} prev
     * @param {HTMLElement} curr
     * @returns {HTMLElement}
     */
    (prev, curr) => {
      /** @type {number} */
      const prevDistance = Math.abs(
        prev.getBoundingClientRect().top + prev.offsetHeight / 2 - viewportCenter
      );

      /** @type {number} */
      const currDistance = Math.abs(
        curr.getBoundingClientRect().top + curr.offsetHeight / 2 - viewportCenter
      );

      return prevDistance < currDistance ? prev : curr;
    }
  );
};

/**
 * Get available scrollable elements.
 *
 * @name utils.getScrollableElements
 * @returns {HTMLElement[]}
 *     Scrollable nodes ordered from most-specific (inner) to most-general (outer).
 *
 * @see https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/mode.js
 */
utils.getScrollableElements = () => {
  /** @type {HTMLElement[]} */
  const nodes = /** @type {HTMLElement[]} */ (
    utils.listElements(
      document.body,
      NodeFilter.SHOW_ELEMENT,
      /**
       * TreeWalker-style filter: return NodeFilter.FILTER_ACCEPT / FILTER_SKIP.
       *
       * @param {Node} node
       * @returns {number}
       */
      (node) => {
        if (!(node instanceof HTMLElement)) {
          return NodeFilter.FILTER_SKIP;
        }

        const n = node;

        const ok =
          (utils.hasScroll(n, "y", 16) && n.scrollHeight > 200) ||
          (utils.hasScroll(n, "x", 16) && n.scrollWidth > 200);

        return ok ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_SKIP;
      }
    )
  );

  nodes.sort(
    /**
     * Sort so inner elements appear before outer elements, otherwise by area.
     *
     * @param {HTMLElement} a
     * @param {HTMLElement} b
     * @returns {number}
     */
    (a, b) => {
      if (b.contains(a)) return 1;
      if (a.contains(b)) return -1;
      return b.scrollHeight * b.scrollWidth - a.scrollHeight * a.scrollWidth;
    }
  );

  const se = document.scrollingElement;

  if (
    se instanceof HTMLElement &&
    (se.scrollHeight > window.innerHeight || se.scrollWidth > window.innerWidth)
  ) {
    nodes.unshift(se);
  }

  return nodes;
};

/**
 * Init scrolling object indexes, and reset scroll nodes event listeners.
 *
 * @name utils.initScrollIndex
 * @returns {void}
 * @see https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/normal.js
 */
utils.initScrollIndex = () => {
  //if (!Array.isArray(scrollNodes) || scrollNodes.length == 0) {
  if (Array.isArray(scrollNodes) && scrollNodes.length > 0) {
    return;
  }
  const nodes = utils.getScrollableElements();

  scrollNodes = nodes;

  /**
   * `addEventListener` expects an `EventListener` whose parameter is `Event`,
   * not `MouseEvent`. We wrap the typed handler to satisfy TS and still keep
   * MouseEvent typing inside `utils.scrollableMousedownHandler`.
   *
   * @type {EventListener}
   */
  const mousedownListener = (evt) => {
    if (evt instanceof MouseEvent) {
      utils.scrollableMousedownHandler(evt);
    }
  };

  nodes.forEach(
    /**
     * @param {HTMLElement} n
     * @returns {void}
     */
    (n) => {
      n.removeEventListener("mousedown", mousedownListener);
      n.addEventListener("mousedown", mousedownListener);

      /* dataset exists on HTMLElement */
      n.dataset.hint_scrollable = "true";
    }
  );

  scrollIndex = 0;
};

/**
 * Check whether a given element supports scrolling in a direction by at least `barSize`.
 *
 * @param {Element} el
 *     Target element to test.
 * @param {"x" | "y"} direction
 *     Scroll axis to test: "x" for horizontal, "y" for vertical.
 * @param {number} barSize
 *     Minimum scroll delta considered "scrollable" (typically scrollbar size, e.g. 16).
 *
 * @returns {boolean}
 *     True if the element can scroll at least `barSize` in the given direction.
 *
 * @example
 * const nodes = utils.listElements(document.body, NodeFilter.SHOW_ELEMENT, function (n) {
 *   return (
 *     (utils.hasScroll(n, "y", 16) && n.scrollHeight > 200) ||
 *     (utils.hasScroll(n, "x", 16) && n.scrollWidth > 200)
 *   );
 * });
 *
 * @see https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/mode.js
 */
utils.hasScroll = (el, direction, barSize) => {
  if (!(el instanceof HTMLElement)) {
    return false;
  }

  /** @type {number} */
  let result = 0;

  if (direction === "y") {
    result = el.scrollTop;

    if (result < barSize) {
      /** @type {number} */
      const origin = el.scrollTop;

      el.scrollTop = el.getBoundingClientRect().height;
      result = el.scrollTop;
      el.scrollTop = origin;
    }

    return result >= barSize;
  }

  /* direction === "x" */
  result = el.scrollLeft;

  if (result < barSize) {
    /** @type {number} */
    const origin = el.scrollLeft;

    el.scrollLeft = el.getBoundingClientRect().width;
    result = el.scrollLeft;
    el.scrollLeft = origin;
  }

  return result >= barSize;
};

/**
 * Handle mousedown events on scrollable elements, updating the active `scrollIndex`
 * based on which scroll node contains the click target.
 *
 * @param {MouseEvent} e
 *     The mousedown event.
 *
 * @returns {void}
 *     This function returns nothing.
 *
 * @see https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/normal.js
 */
utils.scrollableMousedownHandler = (e) => {
  const ct = e.currentTarget;
  if (!(ct instanceof HTMLElement)) return;

  const t = e.target;
  if (!(t instanceof HTMLElement)) return;

  const container = ct;
  const target = t;

  if (!container.contains(target)) return;
  if (!scrollNodes || !Array.isArray(scrollNodes)) return;

  let index = scrollNodes.lastIndexOf(target);

  for (let i = scrollNodes.length - 1; i >= 0 && index === -1; i -= 1) {
    const node = scrollNodes[i];

    if (node !== document.body && node.contains(target)) {
      index = i;
      break;
    }
  }

  if (index !== -1) scrollIndex = index;
};

/** Refresh scrollable elements nodes
 *
 * @return {HTMLElement[] | null}
 * @name utils.refreshScrollableElements
 * @see [normal.refreshScrollableElements](https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/normal.js)
 */
utils.refreshScrollableElements = () => {
  scrollNodes = null;
  utils.initScrollIndex();
  return scrollNodes;
};

/** Reset scroll focused target, including node highlighting
 *
 * Mapped to shortcut `;r`
 *
 * @param {boolean} [highlight=true]
 * @name utils.resetScrollTarget
 * @TODO: Check if changing scrollNodes = null by [] didn't break
 */
utils.resetScrollTarget = (highlight = true) => {
  utils.initScrollIndex();
  if (!scrollNodes || !Array.isArray(scrollNodes)) {
    return;
  }
  if (scrollNodes.length > 0) {
    const scrollNode = scrollNodes[scrollIndex];
    scrollNode.dispatchEvent(utils.mouseDown);
    if (highlight === true) {
      utils.highlightElement(scrollNode);
    }
  }
};

/** Show available scrollable elements hints, and focus chosen one.
 *
 *  Mapped to shortcut `;;`
 *
 *  @name utils.focusScrollTarget
 */
utils.focusScrollTarget = () => {
  api.Hints.create(
    utils.refreshScrollableElements(),
    (el) => {
      el.dispatchEvent(utils.mouseDown);
      utils.highlightElement(el);
    },
    { active: true }
  );
};

/** Dispatch surfingkeys command event
 *
 * @param {string} type
 * @param {object} args
 * @param {Document} [target=document]
 *
 * @name utils.dispatchSKEvent
 * @see [dispatchSKEvent](https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/common/runtime.js)
 */
utils.dispatchSKEvent = (type, args, target) => {
  if (target === undefined) {
    target = document;
  }
  target.dispatchEvent(new CustomEvent(`surfingkeys:${type}`, { detail: args }));
};

/** Front page blur and message printing to indicate user chosen element.
 *
 * Used for example on scrollable focus changing commands/functions, for visual demonstration of
 * new focused element.
 *
 * @param {Element} elm
 * @name utils.highlightElement
 * @see [highlightElement](https://github.com/brookhong/Surfingkeys/blob/master/src/content_scripts/front.js)
 */
utils.highlightElement = (elm) => {
  let rc;
  if (document.scrollingElement === elm) {
    rc = {
      top: 0,
      left: 0,
      width: window.innerWidth,
      height: window.innerHeight,
    };
  } else {
    rc = elm.getBoundingClientRect();
  }
  utils.dispatchSKEvent("front", [
    "highlightElement",
    {
      duration: 200,
      rect: {
        top: rc.top,
        left: rc.left,
        width: rc.width,
        height: rc.height,
      },
    },
  ]);
};
/**
 * List elements under a root node using a NodeIterator, with optional filtering.
 *
 * It also traverses into open shadow roots found on elements.
 *
 * @param {Node} root
 *     Root node to start iteration from (e.g., document.body, Element, ShadowRoot).
 * @param {number} whatToShow
 *     NodeFilter bitmask (e.g., NodeFilter.SHOW_ELEMENT).
 * @param {NodeFilter | ((node: Node) => number) | { acceptNode(node: Node): number }} filter
 *     NodeFilter-compatible filter:
 *     - a NodeFilter object
 *     - a function returning NodeFilter.FILTER_ACCEPT / FILTER_REJECT / FILTER_SKIP
 *     - an object with acceptNode(node): number
 *
 * @returns {Node[]}
 *     List of matching nodes.
 */
utils.listElements = (root, whatToShow, filter) => {
  /** @type {Node[]} */
  const elms = [];

  /**
   * Normalize filter into a NodeFilter-compatible object.
   *
   * @type {NodeFilter}
   */
  const nodeFilter = typeof filter === "function" ? { acceptNode: filter } : filter;

  /** @type {NodeIterator} */
  const iterator = document.createNodeIterator(root, whatToShow, nodeFilter);

  /** @type {Node | null} */
  let current = iterator.nextNode();

  while (current !== null) {
    elms.push(current);

    /*
     * Traverse open shadow roots if present.
     */
    if (current instanceof Element && current.shadowRoot) {
      elms.push(...utils.listElements(current.shadowRoot, whatToShow, filter));
    }

    current = iterator.nextNode();
  }

  return elms;
};

/**
 * Parse given string value, converting its type if it matches other js type notation.
 *
 * For example, "true" is parsed to true (boolean), "24" to 24 (number), etc...
 *
 * @param {string} value
 * @returns {string | number | boolean | object | string | null | undefined}
 * @name utils.parsePrompt
 * @example
 *   typeof utils.parsePrompt("false");
 *   [OUT] boolean
 */
utils.parsePrompt = (value) => {
  const v = value.trim();

  if (/^(true|false)$/i.test(v)) return v.toLowerCase() === "true";
  if (/^null$/i.test(v)) return null;
  if (/^undefined$/i.test(v)) return undefined;
  if (/^-?\d+(\.\d+)?$/.test(v)) return Number(v);

  try {
    // JSON objects / arrays
    return JSON.parse(v);
  } catch {
    return value;
  }
};

/**
 * Find an element by tag name and partial text using several fallback strategies.
 *
 * The function tries, in order:
 *
 * 1. Visible text content:
 *    button text includes "like"
 *
 * 2. data-test attribute:
 *    button[data-test*="like"]
 *
 * 3. aria-label attribute:
 *    button[aria-label*="like"]
 *
 * @param {string} elementType - The HTML element type, such as "button", "a", or "div".
 * @param {string} partialText - Partial text to search for, such as "like" or "Unmute".
 * @returns {HTMLElement | Element | null} The first matching element, or null if no match is found.
 *
 * @example
 * const button = findElementByPartialMatch("button", "like");
 * button?.click();
 *
 * @example
 * const unmuteButton = findElementByPartialMatch("button", "Unmute");
 * unmuteButton?.click();
 */
utils.findElementByPartialMatch = (elementType, partialText) => {
  const normalizedText = partialText.trim().toLowerCase();

  if (!elementType || !normalizedText) {
    return null;
  }

  const elements = [...document.querySelectorAll(elementType)];

  const byTextContent = elements.find((element) =>
    element.textContent.trim().toLowerCase().includes(normalizedText)
  );

  if (byTextContent) {
    return byTextContent;
  }

  const byDataTest = elements.find((element) => {
    const dataTest = element.getAttribute("data-test");

    return dataTest && dataTest.toLowerCase().includes(normalizedText);
  });

  if (byDataTest) {
    return byDataTest;
  }

  const byAriaLabel = elements.find((element) => {
    const ariaLabel = element.getAttribute("aria-label");

    return ariaLabel && ariaLabel.toLowerCase().includes(normalizedText);
  });

  if (byAriaLabel) {
    return byAriaLabel;
  }

  return null;
};


/* Derived settings from JSON */
settings.logMessages = false;

/**
 * @file commands.js
 * @description Defines custom commands functions for SurfingKeys.
 *
 * The code in this script is injected the literally the way it is written, on surfingkeys
 * options.html page, when options.html is setted to load `server.js`.
 *
 * This script is the 2nd injected script to options.html.
 *
 * As defined by surfingkeys extension, to run surfingkeys commands on configurations written in
 * options.html, is necessary to use `api` before the executed function.
 *
 * Since the functions written here will all be written to `options.html`, the functions can
 * be simple defined not being needed to be inside `commands` object. The here formatting using
 * `commands` is simply for better organizing.
 *
 * toggleBlocklist toggleMouseQuery getState addVIMark jumpVIMark appendNonce resetSettings
 * loadSeetingsFromUrl getRecentlyClosed getTopSites getAllURLs getTabs togglePinTab focusTab
 * focusTabByIndex goToLastTab historyTab nextTab previousTab reloadTab closeTab closeTabLeft
 * closeTabRight closeTabsToLeft closeTabsToRight tabOnly closeAudibleTab muteTab openLast
 * duplicateTab getWindows moveToWindow gatherWindows gatherTabs getBookmarkFolders createBookmark
 * filterBookmarksByQuery getBookmarks getHistory addHistories openLink viewSource getSettings
 * updateSettings updateInputHistory setSurfingkeysIcon request requestImageunextFrame moveTab
 * quit createSession openSession deleteSession closeDownloadShelf getDownloads tabURLAccessed
 * getTabURLs getTopURL updateProxy setZoom removeURL localData captureVisibleTab getCaptureSize
 * deleteHistoryOlderThan removeBookmark getBookmark initGist readComment editComment queueURLs
 * getQueueURLs clearQueueURLs getVoices read stopReading openIncognito writeClipboard readClipboard
 * llmRequest getAllLlmProviders connectNative
 *
 * @see Surfingkeys/start/background/start.js
 *
 * download
 * chrome.downloads.download({ url: message.url, saveAs: message.saveAs });
 */

const commands = {};

/**
 * Open vi editor with current clipboard content, writing the editor content on complete to
 * the clipboard.
 *
 * @name commands.editClipboard
 */
commands.editClipboard = () => {
  api.Clipboard.read((c) => {
    api.Front.showEditor(`${c.data}`, (newc) => {
      api.Clipboard.write(newc);
    });
  });
};

/**
 * Open multiple urls present on current clipboard.
 *
 * @name commands.openMultipleYankURL
 */
commands.openMultipleYankURL = () => {
  api.Clipboard.read((response) => {
    if (response) {
      const urls = response.data.split("\n");
      urls.forEach((url) => {
        window.open(url.trim(), "_blank");
      });
    } else {
      api.Front.showBanner("Clipboard is empty or contains no URLs");
    }
  });
};

/**
 * Toggle browser pdf viewer on/off.
 *
 * @name commands.togglePdfViewer
 */
commands.togglePdfViewer = () => {
  chrome.storage.local.get("noPdfViewer", (resp) => {
    if (!resp.noPdfViewer) {
      chrome.storage.local.set({ noPdfViewer: 1 }, () => {
        api.Front.showBanner("PDF viewer disabled.");
      });
    } else {
      chrome.storage.local.remove("noPdfViewer", () => {
        api.Front.showBanner("PDF viewer enabled.");
      });
    }
  });
};

/**
 * Yank all tab URLs to the right/left of the current tab.
 *
 * Parameters
 * ----------
 * direction : string, optional
 *     Which side to yank. Use "right" or "left". Defaults to "left".
 *
 * Notes
 * -----
 * This relies on SurfingKeys `api.RUNTIME("getTabs", ...)` returning an object with `tabs`.
 */
commands.yankTabsDirection = (direction = "left") => {
  /** @type {boolean} */
  let biggerThanCurr = direction === "right" ? false : true;

  /** @type {string} */
  let tabsNames = "";

  /** @type {number} */
  let counter = 0;

  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);

    resp.tabs.forEach(
      /** @param {chrome.tabs.Tab} tab */
      (tab) => {
        if (biggerThanCurr) {
          if (typeof tab.url === "string") {
            tabsNames += `${tab.url} `;
            counter += 1;
          }
        }

        if (tab.active) {
          biggerThanCurr = !biggerThanCurr;
        }
      }
    );

    api.Clipboard.write(tabsNames.trim());
    api.Front.showBanner(`${counter} tabs yanked.`);
  });
};

//commands.closeTabsDirection = (direction = "left") => {
//[>* @type {boolean} <]
//let biggerThanCurr = direction === "right" ? false : true;

//[>* @type {number} <]
//let counter = 0;

//api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
//[>* @type {{ tabs: chrome.tabs.Tab[] }} <]
//const resp = [>* @type {{ tabs: chrome.tabs.Tab[] }} <] (response);

//resp.tabs.forEach(
//[>* @param {chrome.tabs.Tab} tab <]
//(tab) => {
//if (biggerThanCurr) {
//counter += 1;
//}

//if (tab.active) {
//biggerThanCurr = !biggerThanCurr;
//}
//}
//);

//setTimeout(() => {
//api.RUNTIME.repeats = counter;

//if (direction === "right") {
//api.RUNTIME("closeTabRight");
//} else {
//api.RUNTIME("closeTabLeft");
//}
//}, 200);

//api.Front.showBanner(`${counter} tabs closed.`);
//});
//};

/**
 * Count the total number of existing tabs and how many are
 * to the left and right of the current tab.
 *
 * @name commands.countTabs
 */
commands.countTabs = () => {
  /** @type {boolean} */
  let biggerThanCurr = false;

  /** @type {number} */
  let lcounter = 0;

  /** @type {number} */
  let rcounter = 0;

  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);

    resp.tabs.forEach(
      /** @param {chrome.tabs.Tab} tab */
      (tab) => {
        if (biggerThanCurr) {
          rcounter += 1;
        } else {
          lcounter += 1;
        }

        if (tab.active) {
          biggerThanCurr = true;
          lcounter -= 1;
        }
      }
    );

    /** @type {number} */
    const nTabs = resp.tabs.length;

    api.Front.showBanner(`${nTabs} Tabs  |  ${lcounter} left - ${rcounter} right`, 3000);
  });
};

/**
 * Edit chosen hint href url, and open final vi written input.
 *
 * @name commands.editOpenLink
 */
commands.editOpenLink = () => {
  api.Hints.create(
    "a[href]",
    /** @type {string} */
    /** @param {HTMLAnchorElement} a */
    (a) => api.Front.showEditor(a.href, (url) => commands.openLink(url), "url")
  );
};

/**
 * Edit current url in vi mode, and open new url.
 *
 * @TODO: Check vi mode wrong cursor position/bugged
 * @name commands.editAndGoToUrl
 */
commands.editAndGoToUrl = () => {
  const src = window.location.href;
  api.Front.showEditor(src, (url) => commands.openLink(url), "url");
};

/**
 * Hover over with mouseenter given hint element
 * clicking to focus on the chosen one
 */
commands.mouseOver = () => {
  utils.createHints(
    utils.mainHints,
    (el) => {
      el.dispatchEvent(utils.mouseOver);
      el.dispatchEvent(utils.mouseEnter);
      el.dispatchEvent(utils.mouseMove);
      el.focus({ preventScroll: true });
    },
    { tabbed: false, active: true, multipleHits: false }
  );
};
/**
 * Trigger a synthetic hover sequence on an element.
 *
 * Dispatch pointer and mouse hover events without clicking, which can start
 * previews on sites whose thumbnails react to hover.
 *
 * @param {Element} element - Target element to hover.
 * @returns {boolean} Whether the hover sequence was dispatched.
 */
function hoverPreviewElement(element) {
  if (!(element instanceof Element)) {
    return false;
  }

  const rect = element.getBoundingClientRect();
  const clientX = rect.left + rect.width / 2;
  const clientY = rect.top + rect.height / 2;

  /** @type {MouseEventInit & PointerEventInit} */
  const eventInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    view: window,
    clientX,
    clientY,
    screenX: window.screenX + clientX,
    screenY: window.screenY + clientY,
    pointerId: 1,
    pointerType: "mouse",
    isPrimary: true,
  };

  const eventTypes = [
    "pointerover",
    "pointerenter",
    "mouseover",
    "mouseenter",
    "pointermove",
    "mousemove",
  ];

  for (const type of eventTypes) {
    const EventCtor = type.startsWith("pointer") ? PointerEvent : MouseEvent;
    element.dispatchEvent(new EventCtor(type, eventInit));
  }

  return true;
}

/**
 * Remove synthetic hover from an element.
 *
 * @param {Element} element - Target element to unhover.
 * @returns {boolean} Whether the leave sequence was dispatched.
 */
function unhoverPreviewElement(element) {
  if (!(element instanceof Element)) {
    return false;
  }

  const rect = element.getBoundingClientRect();
  const clientX = rect.left + rect.width / 2;
  const clientY = rect.top + rect.height / 2;

  /** @type {MouseEventInit & PointerEventInit} */
  const eventInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    view: window,
    clientX,
    clientY,
    screenX: window.screenX + clientX,
    screenY: window.screenY + clientY,
    pointerId: 1,
    pointerType: "mouse",
    isPrimary: true,
  };

  const eventTypes = ["pointerout", "pointerleave", "mouseout", "mouseleave"];

  for (const type of eventTypes) {
    const EventCtor = type.startsWith("pointer") ? PointerEvent : MouseEvent;
    element.dispatchEvent(new EventCtor(type, eventInit));
  }

  return true;
}

/**
 * Select likely video preview targets on the page.
 *
 * @returns {HTMLElement[]} Matching hoverable elements.
 */
function getVideoPreviewTargets() {
  /** @type {string[]} */
  const selectors = [
    "video",
    "a[href*='watch']",
    "a[href*='/video/']",
    "a[href*='/shorts/']",
    "[data-testid*='video']",
    "[class*='video']",
    "[class*='thumbnail']",
    "img.thumb[data-preview]",
    "[class*='floatbanner']",
    "[class*='ratio-box thumb-lazy']",
    "[id*='video']",
    "[id*='thumbnail']",
    "img[src*='ytimg']",
    "img[alt*='thumbnail' i]",
  ];

  /** @type {HTMLElement[]} */
  const elements = [];
  const seen = new Set();

  for (const element of document.querySelectorAll(selectors.join(","))) {
    if (!(element instanceof HTMLElement)) {
      continue;
    }

    if (seen.has(element)) {
      continue;
    }

    const rect = element.getBoundingClientRect();
    if (rect.width < 40 || rect.height < 30) {
      continue;
    }

    seen.add(element);
    elements.push(element);
  }

  return elements;
}

commands.omniAltUrls = () => {
  const altUrls = [
    {
      title: "Dark Reader",
      url: "moz-extension://a1b6b844-02f5-45a9-bd32-2f05ba7123c6/ui/popup/index.html",
    },
    {
      title: "Addons",
      url: "about:addons",
    },
  ];
  api.Front.openOmnibar({ type: "UserURLs", extra: altUrls });
};

/**
 * Navigate the page by incrementing or decrementing the page number in the URL.
 *
 * @param {"up"|"down"} direction
 */
commands.changePage = (direction) => {
  /** @type {string} */
  const currentUrl = window.location.href;

  /** @type {RegExp} */
  const pageRegex = /(?:\/|\?|&|#|=)(\d+)(?:\/|$|\?|#|&)?/g;

  /** @type {RegExp} */
  const searchRegex = /(\?s=\w*)/g;

  /** @type {NodeListOf<HTMLElement>} */
  const nextBtn = document.querySelectorAll(".post__nav-link.next");

  /** @type {NodeListOf<HTMLElement>} */
  const prevBtn = document.querySelectorAll(".post__nav-link.prev");

  /**
   * Query next/prev links. We merge both selectors because `querySelectorAll(...) || ...`
   * never falls back (NodeList is always truthy even if empty).
   *
   * @type {NodeListOf<HTMLAnchorElement>}
   */
  const nextHref = document.querySelectorAll("a[rel='next'],a[aria-label='Next Page']");

  /** @type {NodeListOf<HTMLAnchorElement>} */
  const prevHref = document.querySelectorAll("a[rel='prev'],a[aria-label='Previous Page']");

  /** @type {boolean} */
  let matchFound = false;

  // Prefer explicit buttons if present.
  if (direction === "up" && nextBtn.length > 0) {
    nextBtn[0].click();
    return;
  }
  if (direction === "down" && prevBtn.length > 0) {
    prevBtn[0].click();
    return;
  }

  // Fall back to rel/aria next/prev anchors, but avoid search pages (example rule from your code).
  if (nextHref.length > 0 && direction === "up" && !searchRegex.test(currentUrl)) {
    window.location.href = nextHref[0].href;
    return;
  }
  if (prevHref.length > 0 && direction === "down" && !searchRegex.test(currentUrl)) {
    window.location.href = prevHref[0].href;
    return;
  }

  // Replace a numeric segment in the URL.
  const replacedUrl = currentUrl.replace(pageRegex, (match, pageNumber) => {
    matchFound = true;

    /** @type {number} */
    const curr = Number.parseInt(pageNumber, 10);

    /** @type {number} */
    const next = direction === "up" ? curr + 1 : curr - 1;

    if (next < 1) {
      api.Front.showBanner("Cannot navigate to a page number less than 1.", 1000);
      return match;
    }

    return match.replace(pageNumber, String(next));
  });

  if (matchFound) {
    window.location.href = replacedUrl;
    return;
  }

  // If no number found, append `page=2` as a fallback.
  const delimiter = currentUrl.includes("?") ? "&" : "?";
  window.location.href = `${currentUrl}${delimiter}page=2`;
};

/**
 * Preview image url source in a floating html window
 *
 * @param {string} iframeSrc - Url to the image src to be previewed
 * @name commands.previewHTML
 */
commands.previewHTML = (iframeSrc) => {
  const existingPreview = document.getElementById("html-preview-overlay");
  if (existingPreview) {
    existingPreview.remove();
  }

  const previewOverlay = document.createElement("div");
  previewOverlay.id = "html-preview-overlay";
  previewOverlay.style.position = "fixed";
  previewOverlay.style.top = "0";
  previewOverlay.style.left = "0";
  previewOverlay.style.width = "100%";
  previewOverlay.style.height = "100%";
  previewOverlay.style.background = "rgba(0, 0, 0, 0.8)";
  previewOverlay.style.zIndex = "10000";
  previewOverlay.style.display = "flex";
  previewOverlay.style.alignItems = "center";
  previewOverlay.style.justifyContent = "center";

  const iframe = document.createElement("iframe");
  iframe.src = iframeSrc;
  iframe.style.width = "90%";
  iframe.style.height = "90%";
  iframe.style.border = "none";
  iframe.style.borderRadius = "4px";

  previewOverlay.addEventListener("click", () => {
    previewOverlay.remove();
    document.removeEventListener("keydown", handleKeydown); // Clean up event listener
  });

  /** @param {KeyboardEvent} event */
  function handleKeydown(event) {
    if (event.key === "Escape" || (event.ctrlKey && event.key === "x")) {
      previewOverlay.remove();
      document.removeEventListener("keydown", handleKeydown); // Clean up event listener
    }
  }

  document.addEventListener("keydown", handleKeydown);

  previewOverlay.appendChild(iframe);
  document.body.appendChild(previewOverlay);
};

/**
 * commands.focusPlayingTab
 * Gets between all tabs for one with playing audio, focusing the first case of it.
 */
commands.focusPlayingTab = () => {
  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);

    resp.tabs.forEach((n) => {
      if (n.audible === true) {
        api.RUNTIME("focusTab", {
          windowId: n.windowId,
          tabId: n.id,
        });
        console.log(n);
        return n;
      }
    });
  });
};

/**
 * commands.focusRandomTab
 *
 * Focus a random tab among the open ones.
 */
/**
 * commands.focusPlayingTab
 * Gets between all tabs for one with playing audio, focusing the first case of it.
 */
commands.focusRandomTab = () => {
  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);
    if (!resp.tabs) {
      return;
    }
    console.log(resp.tabs);

    const randomTab = resp.tabs[Math.floor(Math.random() * resp.tabs.length)];

    if (typeof randomTab.id !== "number") {
      return;
    }

    api.RUNTIME("focusTab", {
      windowId: randomTab.windowId,
      tabId: randomTab.id,
    });
  });
};

/**
 * Open a url link.
 *
 * @name commands.openLink
 * @param {string | URL} url
 *     The URL to open (string or URL object).
 * @param {{ newTab?: boolean, active?: boolean }} [opts={}]
 *     Open options.
 *
 * @example
 * commands.openLink("https://google.com", { newTab: false, active: true })
 */
commands.openLink = (url, { newTab = false, active = true } = {}) => {
  const href = url instanceof URL ? url.href : url;

  if (newTab) {
    api.RUNTIME("openLink", {
      tab: { tabbed: true, active },
      url: href,
    });
    return;
  }

  window.location.assign(href);
};

/**
 * Go to a tab in a given position (first or last tab).
 *
 * @param {string} position
 *     "f" for first tab, "l" for last tab.
 *
 * @name commands.goToTab
 */
commands.goToTab = (position) => {
  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);

    if (!resp.tabs || resp.tabs.length === 0) {
      api.Front.showBanner("No tabs found.", 1000);
      return;
    }

    if (position === "f") {
      const first = resp.tabs[0];
      api.RUNTIME("focusTab", { tabId: first.id, windowId: first.windowId });
      return;
    }

    if (position === "l") {
      /** @type {number} */
      const lastIdx = resp.tabs.length - 1;

      const last = resp.tabs[lastIdx];
      api.RUNTIME("focusTab", { tabId: last.id, windowId: last.windowId });
    }
  });
};

/**
 * Change current video volume.
 *
 * @param {number} level
 *     Delta or absolute volume.
 *     - If `level` is 0 or 1, it is treated as an absolute volume.
 *     - Otherwise it is added to the current volume as a delta.
 *
 * @name commands.changeVolume
 */
commands.changeVolume = (level) => {
  /** @type {NodeListOf<HTMLVideoElement>} */
  const videos = document.querySelectorAll("video");

  videos.forEach(
    /** @param {HTMLVideoElement} video */
    (video) => {
      if (level !== 0 && level !== 1) {
        video.volume = video.volume + level;
      } else {
        video.volume = level;
      }

      // SurfingKeys expects a string message.
      api.Front.showBanner(String(video.volume), 1000);
    }
  );
};

/** Direct mouse clicking on a video element to play it.
 *
 * Useful when other playing methods fail.
 *
 * @name commands.clickVideoPlay
 * @see commands.togglePlayVideo
 */
commands.clickVideoPlay = () => {
  /** @type {string[]} */
  const defaults = [
    ".player-cover",
    ".vjs-big-play-button",
    ".ytp-large-play-button",
    "button[aria-label='Play']",
    "button[title='Play']",
    "[aria-label='Play']",
    ".big-play-button",
    ".btn-play",
    ".icon-play",
    ".fa-play",
  ];

  defaults.forEach((selector) => {
    /** @type {NodeListOf<HTMLElement>} */
    const buttons = document.querySelectorAll(selector);

    if (buttons.length > 0) {
      buttons[0].click();
      return;
    }
  });
};

/**
 * Toggle video play by clicking on play icon.
 * @return number - 0 if success, 1 if failed.
 */
commands.toggleClickPlay = () => {
  const plbtns = [".jw-icon-play", "[data-plyr='play']"];

  /** @type {NodeListOf<HTMLElement>} */
  const btn = document.querySelectorAll(plbtns.join(", "));

  // If any fulscreen element button was found
  if (btn.length !== 0) {
    btn[0].click();
    return 0;
  }

  return 1;
};

/**
 * Sets video to given parameter time.
 * Can be in percentage (0-1 of total video) or secs.
 * fallbacks to user inputs in secs.
 *
 * @param {number} time?
 */
commands.setVideoTime = (time) => {
  const video = utils.findClosestEl("video.vjs-tech") || utils.findClosestEl("video");
  if (!video) {
    return null;
  }
  if (video instanceof HTMLVideoElement) {
    if (!time) {
      const newTime = prompt(`Set video time: (max ${video.duration}`);
      video.currentTime = Number(newTime);
    } else {
      if (time >= 1) {
        const newTime = time;
        video.currentTime = Number(newTime);
      } else {
        const newTime = video.duration * time;
        video.currentTime = Number(newTime);
      }
    }
  }
};

/**
 * Finds video element inside iframe, if exists.
 * @return {HTMLVideoElement | null}
 */
commands.findIframeVideo = () => {
  /** @type {HTMLIFrameElement | null} */
  const iframe = document.querySelector("iframe");

  if (!iframe) {
    return null;
  }

  /** @type {Document | null} */
  const doc = iframe.contentDocument || iframe.contentWindow?.document || null;

  if (!doc) {
    return null;
  }

  /** @type {NodeListOf<HTMLVideoElement>} */
  const videos = doc.querySelectorAll("video");

  if (videos.length === 0) {
    return null;
  }

  return videos[0];
};

/**
 * Change closest video playining state (if playing pause or if paused play).
 *
 * @TODO: Check this function
 *
 * @name commands.togglePlayVideo
 */
commands.togglePlayVideo = () => {
  // Find video element
  const video =
    utils.findClosestEl("video.vjs-tech") ||
    utils.findClosestEl("video") ||
    commands.findIframeVideo();

  // Case no video element
  if (video === null) {
    // Find player html div element
    /** @type {NodeListOf<HTMLElement>} */
    const fpInline = document.querySelectorAll("div[class='fp-ui-inline']");

    // Case no player div element
    if (fpInline.length === 0) {
      // Find play icon button to click
      const rst = commands.toggleClickPlay();
      if (rst === 0) {
        api.Front.showBanner("No video element found!", 500);
      }
      return;
    } else {
      // Player html div element clicking
      fpInline[0].click();
      return;
    }
  }

  // Clicking on video element
  video.dispatchEvent(utils.mouseDown);

  if (video.paused) {
    if (video.getAttribute("onplay") === null) {
      video.setAttribute("onplay", "play");
      commands.clickVideoPlay();
    }
    video.play();
    api.Front.showBanner("Playing", 500);
  } else {
    video.pause();
    api.Front.showBanner("Paused", 500);
  }
  utils.resetScrollTarget(false);
};

/**
 * Toggle video sound mute stete
 *
 * @name commands.toggleMuteVideo
 */
commands.toggleMuteVideo = () => {
  /** @type {HTMLVideoElement | null} */
  const video = utils.findClosestEl("video.vjs-tech") || utils.findClosestEl("video");

  if (video === null) {
    console.log("[SurfingKeys] No video element found to mute.");
    return null;
  }

  video.dispatchEvent(utils.mouseVideo);

  if (video.muted) {
    video.muted = false;
    api.Front.showBanner("Unmuted", 500);
  } else {
    video.muted = true;
    api.Front.showBanner("Muted", 500);
  }
};

// TODO: Check Case 2 of icon fullscreen clicking, perceived cases already toggle fs on f key.
/**
 * Toggle video fullscreen state
 *
 * @name coomands.toggleFullScreenVideo
 * @TODO: Check this function
 */
commands.toggleFullScreenVideo = () => {
  // Case 1
  // Fulscreen button elements to query
  // Priority of elements goes from first (highest) to last (lowest)
  const fsbuttons = [
    ".jw-icon-fullscreen",
    "[data-plyr='fullscreen']",
    "[title='Tela cheia']",
    "[title='Fullscreen']",
    "[title='fullscreen']",
    "[aria-label*='Fullscreen']",
  ];

  /** @type {NodeListOf<HTMLElement>} */
  const btn = document.querySelectorAll(fsbuttons.join(", "));

  // If any fulscreen element button was found
  if (btn.length !== 0) {
    btn[0].click();
    return 0;
  }

  // Case 2
  // Fullscreen button to click, queryed based on child icon of it with name == fullscreen
  const btnicon = Array.from(document.querySelectorAll("button")).find(
    (btn) => btn.querySelector("i.icon")?.textContent.trim() === "fullscreen"
  );

  if (btnicon) {
    btnicon.click();
    return 0;
  }

  // Case 3
  // Player div html element, to set class attributes of fullscreen
  const player = document.querySelectorAll("div[id*='playerDiv']");
  if (player.length !== 0) {
    if (player[0].classList.contains("mgp_fullscreen")) {
      player[0].classList.remove("mgp_fullscreen");
    } else {
      player[0].classList.add("mgp_fullscreen");
    }
    return 0;
  }

  // Case 4
  //const iffs = commands.toggleClickIframeFullscreen();
  //if (iffs === 0) {
  //return 0;
  //}

  // Case 5
  // Video element requesting fulsscreen (vjs-tech and .video)
  /** @type {HTMLVideoElement} */
  const video = utils.findClosestEl("video") || utils.findClosestEl("video.vjs-tech");
  if (!video) {
    alert("no video element found.");
    return 1;
  }
  if (!document.fullscreenElement) {
    if (video.controls) {
      video.controls = true;
    }
    video.requestFullscreen();
  } else {
    document.exitFullscreen();
  }
  return 0;
};

/**
 * Toggle a custom created video control bar.
 *
 * @TODO check this function
 * @name commands.toggleControlBar
 */
commands.toggleControlBar = () => {
  // Case the video is an html5 element type
  /** @type {HTMLMediaElement | null} */
  const plyr = document.querySelector(".plyr");

  if (plyr) {
    if (typeof plyr.ariaExpanded === "string" && plyr.ariaExpanded !== "") {
      plyr.classList.add("plyr--hide-controls");
      plyr.classList.remove("plyr--controls-active");
      plyr.ariaExpanded = "";
    } else {
      plyr.classList.remove("plyr--hide-controls");
      plyr.classList.add("plyr--controls-active");
      plyr.ariaExpanded = "true";
      plyr.dispatchEvent(new Event("mouseenter", { bubbles: true, cancelable: false }));
    }
  }
};

/**
 * Move video forward 10 seconds
 *
 * @name commands.videoForward
 */
commands.videoForward = () => {
  /** @type {HTMLVideoElement | null} */
  const video =
    utils.findClosestEl("video.vjs-tech") ||
    utils.findClosestEl("video") ||
    commands.findIframeVideo();
  if (video) {
    video.focus({ preventScroll: true });
    video.currentTime += 10;
    video.dispatchEvent(new Event("mousemove", { bubbles: true, cancelable: false }));
  }
};

/**
 * Move video backward 10 seconds
 *
 * @name commands.videoBackward
 */
commands.videoBackward = () => {
  /** @type {HTMLVideoElement | null} */
  const video =
    utils.findClosestEl("video.vjs-tech") ||
    utils.findClosestEl("video") ||
    commands.findIframeVideo();
  if (video) {
    video.focus({ preventScroll: true });
    video.currentTime -= 10;
    video.dispatchEvent(new Event("mousemove", { bubbles: true, cancelable: false }));
  }
};

/**
 * Create Surfingkeys hints that hover video thumbnails instead of clicking.
 *
 * @returns {void}
 */
commands.startVideoPreviewHints = () => {
  const targets = getVideoPreviewTargets();

  if (!targets.length) {
    api.Front.showBanner("No video preview targets found.", 1500);
    return;
  }

  api.Hints.create(
    targets,
    /**
     * Hover the selected preview target.
     *
     * @param {Element} element - Chosen hinted element.
     * @returns {void}
     */
    (element) => {
      hoverPreviewElement(element);
    }
  );
};

/**
 * Remove hover from all likely video preview targets.
 *
 * @returns {void}
 */
commands.stopAllVideoPreviews = () => {
  for (const element of getVideoPreviewTargets()) {
    unhoverPreviewElement(element);
  }

  api.Front.showBanner("Stopped preview hovers.", 1200);
};

/**
 * Yank to clipboard selected hint video source url.
 *
 * @name comments.yankVideoSrc
 */
commands.yankVideoSrc = () => {
  /** @type {HTMLVideoElement | null} */
  const video = utils.findClosestEl("video") || utils.findClosestEl("video.vjs-tech");
  if (!video) {
    alert("no video element found.");
    return;
  }
  const videoSource = video.currentSrc || video.src;
  if (!videoSource) {
    alert("no video source found.");
    return;
  }
  api.Clipboard.write(`${videoSource}`);
  api.Front.showBanner(`Yanked url: ${videoSource}`, 1000);
};

/**
 * Download closest video element possible.
 *
 * @name commands.downloadVideoAutomatic
 */
commands.downloadVideoAutomatic = () => {
  /** @type {HTMLVideoElement | null} */
  const video = utils.findClosestEl("video") || utils.findClosestEl("video.vjs-tech");
  if (!video) {
    alert("no video element found.");
    return;
  }
  /** @type {string | null} */
  const videoSource = video.currentSrc || video.src;

  if (!videoSource) {
    alert("no video source found.");
    return;
  }

  const lastPart = videoSource.split("/").pop();
  if (!lastPart) {
    alert("Invalid video URL.");
    return;
  }

  const videoName = lastPart.split("?")[0];
  const videoTitle = document.title || video.getAttribute("title") || videoName;
  const fileName = videoTitle.endsWith(".mp4") ? videoTitle : `${videoTitle}.mp4`;
  const link = document.createElement("a");

  link.download = fileName;
  link.href = videoSource;
  link.title = videoTitle;

  document.body.appendChild(link);

  const videoNew = document.querySelectorAll("video");
  videoNew[0].autoplay = false;
  videoNew[0].pause();
  link.dispatchEvent(utils.mouseVideo);

  document.body.removeChild(link);
};

/**
 * Open download format url of a video, chosen by key hinting.
 */
commands.downloadHintVideo = () => {
  utils.createHints(utils.videoHints, (element) => {
    const regex = /<source\s+[^>]*src=["']([^"']+)["'][^>]*>/i;
    const match = element.innerHTML.match(regex);

    if (!match || !match[1]) {
      api.Front.showBanner("No video source found!", 2000);
      return;
    }

    const videoSource = element.currentSrc || element.src || match[1];

    /** @type {(name: string) => string} */
    const sanitize = (name) => name.replace(/[<>:"/\\|?*]+/g, "_");
    const videoName = match[1].split("/").pop().split("?")[0];
    const videoTitle = document.title || element.getAttribute("title") || videoName;
    const fileName = sanitize(videoTitle.endsWith(".mp4") ? videoTitle : `${videoTitle}.mp4`);

    api.Front.showBanner(`Downloading video: ${videoSource}`, 1500);

    api.RUNTIME("download", {
      url: videoSource,
      filename: fileName,
      saveAs: true, // set to false for auto-download
    });
  });
};

/**
 * Show current playing video total/passed time.
 *
 * @name commands.videoShowTime
 */
commands.videoShowTime = () => {
  /** @type {HTMLVideoElement | null} */
  const video = utils.findClosestEl("video") || utils.findClosestEl("video.vjs-tech");
  if (!video) {
    alert("no video element found.");
    return;
  }
  api.Front.showBanner(`${video.currentTime} / ${video.duration}`, 2000);
};

/*-----
  Github
  -----*/

/**
 * Write git cloning command of current repo to clipboard.
 *
 * @param {string} type - Either "http" or "ssh"
 * @name commands.cloneGitAddress
 */
commands.cloneGitAddress = (type) => {
  const url = window.location.href;
  if (!url.includes("github.com")) {
    console.error("Not a GitHub repository page");
    return null;
  }
  if (type === "http") {
    api.Clipboard.write("git clone " + url);
  } else if (type === "ssh") {
    const path = url.split("github.com/")[1];
    const sshUrl = `git@github.com:${path}.git`;
    const cleanSshUrl = sshUrl.split("/tree")[0].split("/blob")[0];
    api.Clipboard.write("git clone " + cleanSshUrl);
  } else {
    console.error("Type parameter of clone command should be http or ssh!");
  }
};

/**
 * Yank to clipboard current git `{author}/{repo}`
 *
 */
commands.yankGitAuthorAndRepo = () => {
  const url = window.location.href;
  if (!url.includes("github.com/")) {
    console.error("Not a github repository page");
    return null;
  }
  const authorAndRepo = url.split("github.com/")[1];
  api.Clipboard.write(`${authorAndRepo}`);
  return;
};

/**
 * Go to current git repo issues tab.
 */
commands.gitGoToIssues = () => {
  const url = window.location.href;
  const cleanUrl = url.split("/tree")[0].split("/blob")[0];
  const issuesUrl = `${cleanUrl}/issues`;
  window.location.href = issuesUrl;
  return;
};

/**
 * Click to star current git repo
 */
commands.clickStarButton = () => {
  /** @type {HTMLElement | null} */
  const starButton = document.querySelector(
    ".unstarred form button[aria-label^='Star this repository']"
  );

  if (starButton) {
    starButton.click();
    api.Front.showBanner("Starred repo", 900);
  } else {
    console.warn("Star button not found or already starred.");
  }
};

/*-------
  Youtube
  -------*/

/**
 * Like current youtube video
 */
commands.likeYtVideo = () => {
  /** @type {NodeListOf<HTMLElement>} */
  const likeBtn = document.querySelectorAll(".ytLikeButtonViewModelHost");
  if (likeBtn.length === 0) {
    api.Front.showBanner("No like button found.", 1000);
    return;
  }
  const maybe = likeBtn[0].children[0]?.children[0]?.children[0] ?? null;

  if (!(maybe instanceof HTMLElement)) {
    return null;
  }
  maybe.click();
};

/*-----
  Gitlab
  ------*/
/**
 * Yank to clipboard gitlab repo cloning command.
 *
 * @param {string} type - Either "http" or "ssh"
 */
commands.cloneGitLabGnomeAddress = (type) => {
  const url = window.location.href;
  if (!url.includes("gitlab.gnome.org")) {
    console.error("Not a Gnome gitlab repository page");
    return null;
  }
  if (type === "http") {
    api.Clipboard.write("git clone " + url);
    return;
  } else if (type === "ssh") {
    const path = url.split("gitlab.gnome.org/")[1];
    const sshUrl = `git@ssh.gitlab.gnome.org:${path}.git`;
    const cleanSshUrl = sshUrl.split("/tree")[0].split("/blob")[0];
    api.Clipboard.write("git clone " + cleanSshUrl);
    return;
  } else {
    console.error("Type parameter of clone command should be http or ssh!");
    return;
  }
};

/*------
  Google
  ------*/

/**
 * Go to google next search page
 */
commands.googleNextPage = () => {
  /** @type {NodeListOf<HTMLElement>} */
  const nextBtn = document.querySelectorAll("[id=pnnext]");
  if (nextBtn.length > 0) {
    nextBtn[0].click();
  }
};

/**
 * Go to google previous search page
 */
commands.googlePrevPage = () => {
  /** @type {NodeListOf<HTMLElement>} */
  const prevBtn = document.querySelectorAll("[id=pnprev]");
  if (prevBtn.length > 0) {
    prevBtn[0].click();
  }
};

/*-----
  Reddit
  ------*/

/**
 * Toggle nearest upvote button relative to a reference element.
 *
 */
commands.redditLike = () => {
  const closestPost = utils.findClosestEl("shreddit-post,shreddit-comment-action-row");
  if (!closestPost) {
    console.log("[SufingKeys]No valid shadow element");
    return null;
  }
  const shadow = closestPost.shadowRoot;
  if (!shadow) {
    console.log("[SufingKeys]No valid shadow element");
    return;
  }
  /** @type {NodeListOf<HTMLElement>} */
  const btns = shadow.querySelectorAll("button[upvote='']");
  if (btns.length === 0) {
    return null;
  }
  const btn = btns[0];
  const currentPressed = btn.getAttribute("aria-pressed") === "true";
  btn.setAttribute("aria-pressed", String(!currentPressed));
  btn.click();
};

commands.redditPlayButton = () => {
  utils.createHints(
    "button[aria-label='Play'],button[aria-label='Toggle playback']",
    api.Hints.dispatchMouseClick
  );
};

/**
 * Open nearest comments section.
 *
 */
commands.redditComments = () => {
  const closestPost = utils.findClosestEl("shreddit-post");
  if (!closestPost) {
    return null;
  }
  const shadow = closestPost.shadowRoot;
  if (!shadow) {
    console.warn("No Valid Shadow Element");
    return;
  }
  /** @type {NodeListOf<HTMLElement>} */
  const btns = shadow.querySelectorAll("a[name='comments-action-button']");
  if (btns.length === 0) {
    return null;
  }
  const btn = btns[0];
  const currentPressed = btn.getAttribute("aria-pressed") === "true";
  btn.setAttribute("aria-pressed", String(!currentPressed));
  btn.click();
};

commands.redditFold = () => {
  /**
   * Get top-level Reddit comment fold buttons.
   *
   * Returns
   * -------
   * HTMLElement[]
   *     Array of fold buttons (no nulls).
   */
  function getTopLevelCommentsWithChildren() {
    /** @type {NodeListOf<HTMLElement>} */
    const comments = document.querySelectorAll("shreddit-comment");

    /** @type {HTMLElement[]} */
    const buttons = [];

    comments.forEach((comment) => {
      const shadow = comment.shadowRoot;
      if (!shadow) {
        return;
      }

      /** @type {HTMLDetailsElement | null} */
      const details = shadow.querySelector("details[tabindex='-1']");
      if (!details) {
        return;
      }

      /** @type {HTMLButtonElement | null} */
      const btn = details.querySelector("button");
      if (!btn) {
        return;
      }

      buttons.push(btn);
    });

    return buttons;
  }

  utils.createHints(getTopLevelCommentsWithChildren(), (element) => {
    element.click();
  });
};

commands.redditPlay = () => {
  const player = document.querySelector("shreddit-player-2");

  if (!player) {
    console.warn("No Reddit video player found");
    return;
  }

  const shadow = player.shadowRoot;
  if (!shadow) {
    console.warn("Shadow root not found");
    return;
  }

  const video = shadow.querySelector("video");
  if (!video) {
    console.warn("Video element not found inside shadow root");
    return;
  }

  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
};

/**
 * Navigate next/prev on an image carrousell on reddit.
 *
 * @param {string} dir
 *   direction, can be "prev"|"next"
 */
commands.redditNavCarr = (dir) => {
  const currCarr = utils.findClosestEl("gallery-carousel");

  if (!currCarr) {
    console.warn("No Valid Carrousel Gallery found");
    return;
  }

  const shadow = currCarr.shadowRoot;
  if (!shadow) {
    console.warn("No Valid Carrousel Gallery Shadow found");
    return;
  }

  if (`${dir}` === "prev") {
    /** @type {NodeListOf<HTMLButtonElement>} */
    const btns = shadow.querySelectorAll("button[aria-label*='Previous page']");
    if (btns.length === 0) {
      return null;
    }
    const btn = btns[0];
    if (!btn) {
      console.warn("No Valid previous button");
      return;
    } else {
      btn.click();
    }
  } else if (`${dir}` === "next") {
    /** @type {NodeListOf<HTMLButtonElement>} */
    const btns = shadow.querySelectorAll("button[aria-label*='Next page']");
    const btn = btns[0];
    if (!btn) {
      console.warn("No Valid Next button");
      return;
    } else {
      btn.click();
    }
  }
};

commands.muteReddit = () => {
  /** @type {HTMLVideoElement | null} */
  const video = utils.findClosestEl("video") || utils.findClosestEl("video.vjs-tech");
  if (video === null) {
    return null;
  }
  if (video.muted) {
    video.muted = false;
  } else {
    video.muted = true;
  }
};

/**
 * Reddit videos clicking for playing/puasing then.
 *
 * @name commands.redditVideoClick
 */
commands.redditVideoClick = () => {
  const shplay = document.querySelectorAll("shreddit-player")[0];
  const shadow = shplay.shadowRoot;
  if (!shadow) {
    console.warn("No Valid Shadow Element");
    return;
  }
  const video = shadow.querySelectorAll("video")[0];
  if (!video) {
    console.warn("No Valid video Element");
    return;
  }
  video.click();
};

/*------
  Others
  ------*/

// Dev / Debug

/**
 * Ginven user input runtime and args, runs and logs it.
 *
 * @name commands.debugInputRuntime
 * @example
 *  commands.debugInputRuntime();
 *  [INPUT]: exec/openLink/'{"url": "google.com"}'
 */
commands.debugInputRuntime = async () => {
  //api.Front.showBanner("Runtime: <Type(exec/log)>/<COMMAND>/{JSON obj args}", 2500);
  //const runinput = await utils.getEditorInput();
  const runinput = prompt("Runtime: <Type(exec/log)>|<COMMAND>,{JSON obj args}");
  const cmd = runinput?.includes("|") ? runinput?.split("|") : runinput?.trim().split(/\s+/);
  if (!cmd) {
    return null;
  }
  if (cmd.length === 1) {
    if (cmd[0] === "exec" || cmd[0] === "log") {
      api.Front.showBanner(`Wrong format! cmd of length 1 cannot be ${cmd[0]}.`, 2000);
      return null;
    } else {
      api.RUNTIME(cmd[0]);
      return;
    }
  }
  if (cmd.length === 2) {
    if (cmd[0] === "exec") {
      api.RUNTIME(cmd[1]);
      return;
    }
    if (cmd[0] === "log") {
      api.RUNTIME(cmd[1], {}, (resp) => {
        console.log(resp);
      });
      return;
    }
    /** @type {string | any} */
    const parsedParam = cmd.slice(1).map(utils.parsePrompt);
    console.log(`parsedParam: ${parsedParam}\ntype: ${typeof parsedParam}`);
    console.log(...parsedParam);
    api.RUNTIME(cmd[0], ...parsedParam);
    return;
  }
  if (cmd.length === 3) {
    if (cmd[0] === "exec") {
      /** @type {string | any} */
      const parsedParam = cmd.slice(2).map(utils.parsePrompt);
      api.RUNTIME(cmd[1], parsedParam);
      return;
    }
    if (cmd[0] === "log") {
      /** @type {string | any} */
      const parsedParam = cmd.slice(2).map(utils.parsePrompt);
      api.RUNTIME(cmd[1], ...parsedParam, (resp) => {
        console.log(resp);
      });
      return;
    }
    /** @type {string | any} */
    const parsedParams = cmd.slice(1).map(utils.parsePrompt);
    //const parsedParama = utils.parsePrompt(cmd[1]);
    //const parsedParamb = utils.parsePrompt(cmd[2]);
    api.RUNTIME(cmd[0], ...parsedParams);
    return;
  }
};

/**
 * Ginven user input SKEvent and args, runs and logs it.
 *
 * @name commands.debugInputSKEvent
 * @example
 *  commands.debugInputSKEvent();
 *  [INPUT]: "api clipboard:write teste"
 */
commands.debugInputSKEvent = () => {
  const cmd = prompt("SKevent [type front|user|api...] [command args*]")?.split(" ");
  if (!cmd) {
    return null;
  }
  if (cmd.length === 1) {
    utils.dispatchSKEvent(cmd[0]);
    return;
  }
  const converted = cmd
    .splice(1) // skip first
    .map(utils.parsePrompt);

  console.log(`${cmd[0]}, ${converted}`);
  utils.dispatchSKEvent(cmd[0], converted);
};

/**
 * Create hints based on user inputted css selector args.
 *
 * @name commands.debugInputCreateHints
 */
commands.debugInputCreateHints = () => {
  //const input = await utils.getEditorInput();
  const regex = /(utils.)\w+/gi;
  /** @type {string | null} */
  const input = prompt("Css selector:");
  /** @type {string[] | null} */
  const selectorList = input ? input.trim().split(/\s+/) : null;

  if (!selectorList) {
    return null;
  }

  /** @type {string[]} */
  const cmd = [];

  selectorList.forEach((cssitem) => {
    const match = cssitem.match(regex);

    if (match) {
      const hintname = cssitem.split(".")[1]?.toString();
      /** @type {string} */
      if (Object.prototype.hasOwnProperty.call(utils, hintname)) {
        const selutils = typeof utils[hintname] === "string" ? utils[hintname] : "";
        /** @type {string} */
        cmd.push(selutils);
      } else {
        api.Front.showBanner(`Invalid ${input}; utils. starting element don't exist`);
        return;
      }
    } else {
      cmd.push(cssitem);
    }
  });

  const cssSelector = cmd.join(",");
  utils.createHints(
    cssSelector,
    (element) => {
      if (!(element instanceof Element)) {
        console.log(element);
        api.Front.showBanner("Invalid hinted element.", 2000);
        return;
      }

      const el = element;
      /** @type { NamedNodeMap | HTMLElement | HTMLAnchorElement | HTMLInputElement | HTMLImageElement } */
      const attrs = el.attributes;
      const attrsStr = Array.from(attrs)
        .map((attr) => `${attr.name}="${attr.value}"`)
        .join("\n");

      /** @type {string[]} */
      const extra = [];

      if (el instanceof HTMLAnchorElement) {
        el.focus();
        extra.push(`Href: ${el.href}`);
      }

      if (el instanceof HTMLImageElement) {
        el.focus();
        extra.push(`Src: ${el.src}`);
        extra.push(`Alt: ${el.alt}`);
      }

      if (el instanceof HTMLInputElement) {
        el.focus();
        extra.push(`Type: ${el.type}`);
        extra.push(`Name: ${el.name}`);
        extra.push(`Value: ${el.value}`);
      }

      if (el instanceof HTMLElement) {
        el.focus();
        extra.push(`Class: ${el.className}`);
        extra.push(`Title: ${el.title}`);
        extra.push(`Tag: ${el.tagName}`);
      } else {
        extra.push(`Tag: ${el.tagName}`);
      }

      const msg = [attrsStr, "", ...extra].filter(Boolean).join("\n");
      console.log(msg);
      //el.dispatchEvent(new Event("mouseenter", { bubbles: true, cancelable: false }));
      el.dispatchEvent(utils.mouseClick);
    },
    { tabbed: false, active: true, multipleHits: true }
  );
};

/**
 * Given user input, run SurfingKeys functions (from api/utils/commands) with given args.
 *
 * Input format
 * ------------
 * - "debug <module>"
 * - "debug <module> <command>"
 * - "<module> <command> [args...]"
 *
 * @name commands.debugRunSkFn
 */
commands.debugRunSkFn = async () => {
  /** @type {Record<string, unknown>} */
  const modules = {
    api,
    utils,
    commands,
    visual: api.Visual,
    normal: api.Normal,
    front: api.Front,
    hints: api.Hints,
    clipboard: api.Clipboard,
    tabopenlink: api.tabOpenLink,
    getclickableelements: api.getClickableElements,
    runtime: api.RUNTIME,
    readtext: api.readText,
  };

  /** @type {string | null} */
  //const input = prompt(
  //"[<module>: debug|api|utils|commands|visual|normal|front] [<command>] [args*?]"
  //);
  api.Front.showBanner(
    "[<module>: debug|api|utils|commands|visual|normal|front] [<command>] [args*?]",
    5000
  );
  const input = await utils.getEditorInput();

  /** @type {string[] | null} */
  const cmd = input ? input.trim().split(/\s+/) : null;

  if (!cmd || cmd.length === 0) {
    return;
  }

  // Debug mode
  if (cmd[0] === "debug") {
    const modName = cmd[1];
    const fnName = cmd[2];

    if (!modName) {
      console.log(modules);
      return;
    }

    const mod = modules[modName];
    if (cmd.length === 2) {
      console.log(mod);
      return;
    }

    if (cmd.length === 3) {
      if (mod && typeof mod === "object") {
        if (Object.prototype.hasOwnProperty.call(mod, fnName)) {
          // @ts-ignore - dynamic property access is intended in this debug helper
          console.log(mod[fnName]);
          return;
        }
      }
      console.log(undefined);
      return;
    }

    return;
  }

  // Run mode: "<module> <command> [args...]"
  const modName = cmd[0];
  const fnName = cmd[1];

  if (!modName) {
    return;
  }

  const mod = modules[modName];

  if (!fnName) {
    console.log(mod);
    return;
  }

  if (!mod || (typeof mod !== "object" && typeof mod !== "function")) {
    console.log(undefined);
    return;
  }

  /** @type {unknown} */
  // @ts-ignore - dynamic index access is intended
  const fn = mod[fnName];

  if (typeof fn !== "function") {
    console.log(fn);
    return;
  }

  if (cmd.length > 2) {
    const args = cmd.slice(2).map(utils.parsePrompt);
    fn(...args);
    return;
  }

  fn();
};

// modules/tabGroups.js
commands.TabGroups = () => {
  api.RUNTIME("getTabs", { queryInfo: { currentWindow: true } }, (response) => {
    /** @type {{ tabs: chrome.tabs.Tab[] }} */
    const resp = /** @type {{ tabs: chrome.tabs.Tab[] }} */ (response);
    const tabs = resp.tabs.filter((t) => typeof t.groupId === "number" && t.groupId !== -1);
    const map = new Map();

    for (const tab of tabs) {
      if (!map.has(tab.groupId)) {
        map.set(tab.groupId, []);
      }
      map.get(tab.groupId).push(tab);
    }
    console.log(map);
    return map;
  });
};

/**
 * Copy nearest code block element.
 */
commands.copyCodeBlock = () => {
  /** @type {HTMLButtonElement | null} */
  const btn = utils.findClosestEl(utils.codeBlockHints);
  if (!btn) {
    api.Front.showBanner("no code block found.", 500);
    return;
  }
  btn.click();
  api.Front.showBanner("Code block yanked.", 500);
  return;
};

/**
 * Pick the most appropriate URL from an element, preferring media `src` when applicable.
 *
 * @param {Element} el
 *     The hinted element.
 *
 * @returns {string | null}
 *     A best-effort absolute URL if resolvable; otherwise null.
 */
function pickBestUrlFromElement(el) {
  /**
   * Resolve a possibly-relative URL against the current document location.
   *
   * @param {string | null} raw
   *     URL candidate.
   *
   * @returns {string | null}
   *     Absolute URL when possible; otherwise null.
   */
  function toAbsolute(raw) {
    if (raw === null) {
      return null;
    }

    const trimmed = raw.trim();
    if (!trimmed) {
      return null;
    }

    if (/^(data|blob|mailto|tel|javascript):/i.test(trimmed) || trimmed.startsWith("#")) {
      return trimmed;
    }

    try {
      return new URL(trimmed, document.baseURI).toString();
    } catch {
      return trimmed;
    }
  }

  /**
   * Extract the first URL candidate from a srcset string.
   *
   * @param {string | null} srcset
   *     The srcset attribute value.
   *
   * @returns {string | null}
   *     First URL candidate, or null.
   */
  function firstFromSrcset(srcset) {
    if (srcset === null) {
      return null;
    }

    /** @type {string[]} */
    const candidates = srcset
      .split(",")
      .map(
        /**
         * @param {string} part
         * @returns {string}
         */
        (part) => part.trim()
      )
      .filter(
        /**
         * @param {string} part
         * @returns {boolean}
         */
        (part) => Boolean(part)
      );

    if (candidates.length === 0) {
      return null;
    }

    /** @type {string} */
    const first = candidates[0];

    /** @type {string} */
    const urlPart = first.split(/\s+/)[0];

    return urlPart ? urlPart.trim() : null;
  }

  /* Media elements */
  if (el instanceof HTMLImageElement) {
    return (
      toAbsolute(el.currentSrc || el.src) ||
      toAbsolute(firstFromSrcset(el.getAttribute("srcset"))) ||
      toAbsolute(el.getAttribute("data-src"))
    );
  }

  if (el instanceof HTMLVideoElement || el instanceof HTMLAudioElement) {
    return toAbsolute(el.currentSrc || el.src) || toAbsolute(el.getAttribute("data-src"));
  }

  if (
    el instanceof HTMLSourceElement ||
    el instanceof HTMLTrackElement ||
    el instanceof HTMLIFrameElement ||
    el instanceof HTMLEmbedElement ||
    el instanceof HTMLScriptElement
  ) {
    return toAbsolute(el.src) || toAbsolute(el.getAttribute("src"));
  }

  /* Link-like elements */
  if (el instanceof HTMLAnchorElement || el instanceof HTMLAreaElement) {
    return toAbsolute(el.href) || toAbsolute(el.getAttribute("href"));
  }

  if (el instanceof HTMLLinkElement) {
    return toAbsolute(el.href) || toAbsolute(el.getAttribute("href"));
  }

  /* Generic fallback */
  /** @type {string[]} */
  const attrCandidates = [
    "src",
    "data-src",
    "poster",
    "srcset",
    "href",
    "data-href",
    "data-url",
    "url",
    "data-original",
    "data-lazy-src",
    "data-src-url",
  ];

  for (/** @type {number} */ let i = 0; i < attrCandidates.length; i += 1) {
    /** @type {string} */
    const attr = attrCandidates[i];

    /** @type {string | null} */
    const raw = el.getAttribute(attr);
    if (raw === null) {
      continue;
    }

    if (attr === "srcset") {
      const fromSet = firstFromSrcset(raw);
      const abs = toAbsolute(fromSet);
      if (abs) {
        return abs;
      }
      continue;
    }

    const abs = toAbsolute(raw);
    if (abs) {
      return abs;
    }
  }

  return null;
}

/**
 * Show hints on URL-bearing elements and copy the most appropriate URL to the clipboard.
 *
 * It prefers:
 * - `src` for media elements (img, video, audio, source, track, iframe, embed, script)
 * - `href` for link-like elements (a, area, link)
 * - `srcset` for responsive images when there is no `src`
 * - common URL-carrying attributes on generic elements (`href`, `src`, `data-src`, etc.)
 */
commands.copyLinks = () => {
  /**
   * Hint callback.
   *
   * @param {Element} el
   *     The hinted DOM element.
   */
  api.Hints.create(utils.linkHints, (el) => {
    const url = pickBestUrlFromElement(el);

    if (!url) {
      api.Front.showBanner("No URL found for hinted element.", 1000);
      return;
    }

    api.Clipboard.write(url);
    api.Front.showBanner(`Yanked: ${url}`, 1000);
  });
};

commands.copyMultipleLinks = () => {
  /**
   * Hint callback.
   *
   * @param {Element} el
   *     The hinted DOM element.
   */
  /** @type {string[]} */
  const collectedUrls = [];
  api.Hints.create(
    utils.linkHints,
    (el) => {
      /** @type {string | null} */
      const url = pickBestUrlFromElement(el);

      if (!url) {
        api.Front.showBanner("No URL found for hinted element.", 1000);
        return;
      }

      collectedUrls.push(url);

      api.Clipboard.write(collectedUrls.join("\n"));
      api.Front.showBanner(`${collectedUrls.length} link(s) Yanked`, 1000);
    },
    {
      /** Enable multi-selection (SurfingKeys feature). */
      multipleHits: true,
    }
  );
};

// TODO: Check for extending allowed dispatchRightClick given param element types.
/**
 * Open a synthetic contextmenu event on an element.
 *
 * @param {Element} element - Target element.
 * @returns {boolean} Whether the event was dispatched.
 */
commands.dispatchRightClick = (element) => {
  if (!(element instanceof Element)) {
    return false;
  }

  const rect = element.getBoundingClientRect();
  const clientX = Math.floor(rect.left + rect.width / 2);
  const clientY = Math.floor(rect.top + rect.height / 2);

  return element.dispatchEvent(
    new MouseEvent("contextmenu", {
      bubbles: true,
      cancelable: true,
      composed: true,
      button: 2,
      buttons: 2,
      clientX,
      clientY,
      screenX: window.screenX + clientX,
      screenY: window.screenY + clientY,
      view: window,
    })
  );
};


/**
 * @file autobots.js
 * @description Provides automation / bots like web js commands.
 *
 *
 */

/**
 *
 * @interface RelativePoint {
 *   rx: number;
 *   ry: number;
 * }
 *
 * @interface PointLike{
 *   rx: number;
 *   ry: number;
 *   col: number;
 *   row: number;
 * }
 *
 * @interface TargetLike{
 *   rx: number;
 *   ry: number;
 *   el: HTMLElement;
 * }
 *
 * @typedef { HTMLElement | {rx: number, ry: number} } MaybeTarget - Possible candidates for targets
 *
 */
const autobots = {};

/**
 * Wait for the given amount of milliseconds.
 *
 * @param {number} ms
 * @returns {Promise<void>}
 */
autobots.sleep = (ms) => {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
};

/**
 * Return the page Flutter host.
 *
 * @returns {HTMLElement}
 */
function getFlutterViews() {
  const view = document.querySelector("flutter-view, canvas, flt-glass-pane, flt-scene");
  if (!(view instanceof HTMLElement)) {
    throw new Error("flutter-view not found.");
  }

  return view;
}

/**
 * Return the current Flutter host rectangle.
 *
 * @returns {DOMRect}
 */
function getFlutterViewRect() {
  return getFlutterViews().getBoundingClientRect();
}

/**
 * Return the currently opened video element, if any.
 *
 * @returns {HTMLVideoElement | null}
 */
function getOpenedVideo() {
  /** @type {HTMLVideoElement | null} */
  const video = document.querySelector("#ima-video-element") || document.querySelector("video");

  return video;
}

/**
 * Wait for a video element to appear.
 *
 * @param {number} timeoutMs
 * @returns {Promise<HTMLVideoElement | null>}
 */
async function waitForVideo(timeoutMs = 2500) {
  const start = Date.now();

  while (Date.now() - start < timeoutMs) {
    const video = getOpenedVideo();

    if (video) {
      return video;
    }

    await autobots.sleep(100);
  }

  return null;
}

/**
 * Convert relative coordinates inside flutter-view into viewport coordinates.
 *
 * @param {number} rx
 * @param {number} ry
 * @returns {RelativePoint}
 */
autobots.getRelativePoint = (rx, ry) => {
  const rect = getFlutterViewRect();

  return {
    rx: rect.left + rect.width * rx,
    ry: rect.top + rect.height * ry,
  };
};

/**
 * Return the document coordinates of an element.
 *
 * @param {HTMLElement} element
 * @returns {{ x: number, y: number }}
 */
function getElementPageXY(element) {
  const rect = element.getBoundingClientRect();

  return {
    x: rect.left + window.scrollX,
    y: rect.top + window.scrollY,
  };
}

/**
 * @typedef {HTMLElement & {
 *   rect: {
 *     left: number,
 *     top: number,
 *     width: number,
 *     height: number
 *   }
 * }} RectElement
 */

/**
 * Return the center coordinates of an element rect.
 *
 * @param {RectElement | null | undefined} element - Element containing a rect
 *   object with position and size fields.
 * @returns {{rx: number, ry: number} | undefined} Center coordinates, or
 *   undefined when the input is invalid.
 */
autobots.getElementCenter = (element) => {
  if (
    !element?.rect ||
    typeof element.rect.left !== "number" ||
    typeof element.rect.top !== "number" ||
    typeof element.rect.width !== "number" ||
    typeof element.rect.height !== "number"
  ) {
    console.log(
      "[SK-CONF] autobots.getElementCenter failed to run. Given parameter does not have a valid 'rect' attribute."
    );
    return;
  }

  return {
    rx: element.rect.left + element.rect.width / 2,
    ry: element.rect.top + element.rect.height / 2,
  };
};

/**
 * Gets a complete flutter element to be used on actions like clicking, based on passed parameters.
 * Given target parameter needs either rx and ry coordinates, or to be an HTMLElement node.
 *
 * @param {MaybeTarget | any} target
 * @returns {TargetLike | null}
 *
 */
autobots.assignTarget = (target) => {
  if (target instanceof HTMLElement) {
    const rect = getElementPageXY(target);
    return { el: target, rx: rect.x, ry: rect.y };
  }
  if (target.rx && target.ry) {
    const coords =
      target.rx < 1 && target.ry < 1 ? autobots.getRelativePoint(target.rx, target.ry) : target;
    if (!coords.rx || !coords.ry) {
      console.log(
        "Error during x,y pos values conversion/checking from relative to position page."
      );
      console.log(`Originals: rx: ${target.rx}; ry: ${target.ry}`);
      console.log(`Converted: rx: ${coords.rx}; ry: ${coords.ry}`);
      return null;
    }
    const elements = document.elementsFromPoint(coords.rx, coords.ry);
    const element = elements.find((item) => item instanceof HTMLElement) ?? null;
    if (element) {
      return { el: element, rx: coords.rx, ry: coords.ry };
    } else {
      console.log(`Found elements don't match any HTMLElement!\n${elements}`);
      return null;
    }
  }
  console.log(
    `Given element target don't have correct format!\nIt should be either {rx: number, ry: number} or HTMLElement\nPassed param: ${target}`
  );
  return null;
};

/**
 * Click given coordinates flutter page position.
 *
 * @param {MaybeTarget| null} target
 * @returns {void}
 */
autobots.flutterClickAt = (target) => {
  //const target = document.elementFromPoint(x, y) || document.querySelector("canvas, flt-glass-pane, flt-scene");
  console.log(target);
  const completeTarget = autobots.assignTarget(target);

  if (!completeTarget) {
    return;
  }
  console.log(completeTarget);
  const pointerInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    clientX: completeTarget.rx,
    clientY: completeTarget.ry,
    pointerId: 1,
    pointerType: "mouse",
    isPrimary: true,
    button: 0,
    buttons: 1,
  };

  const mouseInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    clientX: completeTarget.rx,
    clientY: completeTarget.ry,
    button: 0,
    buttons: 1,
  };

  completeTarget.el.dispatchEvent(new PointerEvent("pointerover", pointerInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerenter", pointerInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerdown", pointerInit));
  completeTarget.el.dispatchEvent(new MouseEvent("mousedown", mouseInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerup", { ...pointerInit, buttons: 0 }));
  completeTarget.el.dispatchEvent(new MouseEvent("mouseup", { ...mouseInit, buttons: 0 }));
  completeTarget.el.dispatchEvent(new MouseEvent("click", { ...mouseInit, buttons: 0 }));
};

/**
 * Dispatch a mouse and pointer click sequence at viewport coordinates.
 *
 * @param {TargetLike| null} target
 * @returns {void}
 */
autobots.flutterPointerClickAt = (target) => {
  const completeTarget = autobots.assignTarget(target);

  if (!completeTarget) {
    return;
  }
  console.log(target);
  console.log(completeTarget);
  const pointerDownInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    clientX: completeTarget.rx,
    clientY: completeTarget.ry,
    pointerId: 1,
    pointerType: "mouse",
    isPrimary: true,
    button: 0,
    buttons: 1,
  };

  const pointerUpInit = {
    ...pointerDownInit,
    buttons: 0,
  };

  const mouseDownInit = {
    bubbles: true,
    cancelable: true,
    composed: true,
    clientX: completeTarget.rx,
    clientY: completeTarget.ry,
    button: 0,
    buttons: 1,
  };

  const mouseUpInit = {
    ...mouseDownInit,
    buttons: 0,
  };

  if (target instanceof HTMLElement) {
    target.focus({ preventScroll: true });
  }

  completeTarget.el.dispatchEvent(new PointerEvent("pointerover", pointerDownInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerenter", pointerDownInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerdown", pointerDownInit));
  completeTarget.el.dispatchEvent(new MouseEvent("mousedown", mouseDownInit));
  completeTarget.el.dispatchEvent(new PointerEvent("pointerup", pointerUpInit));
  completeTarget.el.dispatchEvent(new MouseEvent("mouseup", mouseUpInit));
  completeTarget.el.dispatchEvent(new MouseEvent("click", mouseUpInit));
};

/**
 * Test whether a relative point inside flutter-view opens a video.
 *
 * @param {number} rx
 * @param {number} ry
 * @param {number} timeoutMs
 * @returns {Promise<boolean>}
 */
autobots.testFlutterVideoPoint = async (rx, ry, timeoutMs = 2500) => {
  //const point = flutterPoint(rx, ry);
  const target = document.elementFromPoint(rx, ry);
  console.log(`Obtained document element target: ${target}`);
  autobots.flutterPointerClickAt({ rx, ry });

  const video = await waitForVideo(timeoutMs);
  return Boolean(video);
};

/**
 * Build a grid of relative points inside the central usable area of flutter-view.
 *
 * @param {number} columns
 * @param {number} rows
 * @param {number} left
 * @param {number} top
 * @param {number} right
 * @param {number} bottom
 * @returns {Array<PointLike>}
 */
function buildUIGrid(columns = 2, rows = 4, left = 0.1, top = 0.18, right = 0.9, bottom = 0.9) {
  const points = [];

  for (let row = 0; row < rows; row += 1) {
    for (let col = 0; col < columns; col += 1) {
      const rx = left + ((col + 0.5) * (right - left)) / columns;
      const ry = top + ((row + 0.5) * (bottom - top)) / rows;

      points.push({ rx, ry, col, row });
    }
  }

  return points;
}

/**
 * Find all grid points that open a video.
 *
 * @param {number} [columns=2]
 * @param {number} [rows=4]
 * @param {number} [timeoutMs=2000]
 * @param {boolean} [findAll=false]
 * @returns {Promise<PointLike| Array<PointLike>>}
 */
autobots.findPageVideoGridPoints = async (
  columns = 2,
  rows = 4,
  timeoutMs = 2000,
  findAll = false
) => {
  const points = buildUIGrid(columns, rows);
  const matches = [];

  for (const point of points) {
    console.log("Testing grid point:", point);

    const ok = await autobots.testFlutterVideoPoint(point.rx, point.ry, timeoutMs);

    if (ok) {
      if (findAll === true) {
        matches.push(point);
      } else {
        return point;
      }
    }
  }

  return matches;
};

/**
 * Return visible Flutter semantics nodes with geometry.
 *
 * @param {string|null|undefined|boolean} hostSelector
 * @param {Object.<string, RegExp|string>|null|undefined} queryFilter
 * @returns {Array<{
 *   index: number,
 *   tag: string,
 *   text: string,
 *   ariaLabel: string | null,
 *   role: string | null,
 *   rect: { left: number, top: number, width: number, height: number }
 * }>}
 */
autobots.debugInterface = (hostSelector, queryFilter) => {
  let host;
  if (hostSelector) {
    hostSelector =
      typeof hostSelector === "string" ? hostSelector : "flutter-view flt-semantics-host";
    host = document.querySelector(hostSelector);
  } else {
    host = document;
  }
  if (!host) {
    return [];
  }

  const allNodes = host.querySelectorAll("*");

  let nodes;
  if (queryFilter === null || Object.keys(queryFilter).length === 0) {
    nodes = allNodes;
  } else {
    nodes = utils.filterNodesByFieldsSafe(allNodes, queryFilter);
  }
  //* @type {Array<{index: number; tag: string; text: string; ariaLabel: string | null; role: string | null; rect: { left: number, top: number, width: number, height: number };}>}
  const out = [];
  nodes.forEach((node, index) => {
    const text = (node.textContent || "").trim();
    const rect = node.getBoundingClientRect();
    out.push({
      index,
      provider: node.getAttribute("provider"),
      tag: node.tagName.toLowerCase(),
      text,
      ariaLabel: node.getAttribute("aria-label"),
      role: node.getAttribute("role"),
      rect: {
        left: rect.left,
        top: rect.top,
        width: rect.width,
        height: rect.height,
      },
    });
  });
  return { out: out, nodes: nodes };
};

autobots.clickreddit = () => {
  const embeds = autobots.debugInterface(false, { localName: "shreddit-embed" });
  const nodes = embeds.nodes[0];
  console.log(`Obtained embeded nodes: ${nodes}`);
  const out = embeds.out[0];
  const paramdu = { rect: out.rect };
  const posdu = autobots.getElementCenter(paramdu);
  console.log(posdu);
  //{ x: rect.left + (rect.width / 2), y: rect.top + (rect.height / 2)},
  //if (rect.width <= 0 || rect.height <= 0) {
  //console.log("NNNNN");
  //return;
  //}
  const elPos = document.elementsFromPoint(posdu.rx, posdu.ry);
  elPos.forEach((newel) => {
    newel.click();
    //autobots.flutterPointerClickAt({rx: posdu.rx, ry: posdu.ry, newel});
  });
  //autobots.flutterPointerClickAt({rx: posdu.rx, ry: posdu.ry, nodes})
  //console.log(elPos);
};
//console.log(elPos);
//const pointerInit = {
//bubbles: true,
//cancelable: true,
//composed: true,
//clientX: posdu.rx,
//clientY: posdu.ry,
//pointerId: 1,
//pointerType: "mouse",
//isPrimary: true,
//button: 0,
//buttons: 1,
//};

//const mouseInit = {
//bubbles: true,
//cancelable: true,
//composed: true,
//clientX: posdu.rx,
//clientY: posdu.ry,
//button: 0,
//buttons: 1,
//};

//node.dispatchEvent(new PointerEvent("pointerover", pointerInit));
//node.dispatchEvent(new PointerEvent("pointerenter", pointerInit));
//node.dispatchEvent(new PointerEvent("pointerdown", pointerInit));
//node.dispatchEvent(new MouseEvent("mousedown", mouseInit));
//node.dispatchEvent(new PointerEvent("pointerup", { ...pointerInit, buttons: 0 }));
//node.dispatchEvent(new MouseEvent("mouseup", { ...mouseInit, buttons: 0 }));
//node.dispatchEvent(new MouseEvent("click", { ...mouseInit, buttons: 0 }));
//})
//return out;
//};

/**
 * Gets specific clickable flutter target elements, being flt-semantic buttons.
 *
 */
autobots.getFlutterClickables = () => {
  /** @type {string[]} */
  const extras = [];
  /** @type {HTMLElement | null} */
  const fv = document.querySelector("flutter-view");
  if (fv && fv.click) {
    extras.push(`fv: ${fv}`);
    fv.click();
  }
  //fv?.attachShadow();   Error
  /** @type {HTMLElement | null} */
  const fltHost = document.querySelector("flt-announcement-host");
  if (fltHost) {
    extras.push(`fltHost: ${fltHost}`);
    if (fltHost.click) {
      fltHost.click();
    }
    if (fltHost.focus) {
      fltHost.focus();
    }
  }
  /** @type {HTMLElement | null} */
  const maybeButton = document.body.querySelector("[role='button']");
  if (maybeButton && maybeButton.click) {
    extras.push(`maybeButton: ${maybeButton}`);
    maybeButton.click();
  }
  //acccd = document.querySelectorAll("flt-semantics")
  //document.querySelectorAll("flt-embedding")
  document.querySelectorAll("[id='flutter_container']");

  /** @type {NodeListOf<HTMLElement> | null} */
  const targetEls = document.querySelectorAll("flt-semantics[id^='flt-semantic'][role='button']");
  // I may try if needed, to iterate over then, trying to find correct ones by
  // asserting getBoundingClientRect is not to small.
  // At first did the easy, only exclude first element, because its the case of the developement
  // site.
  //console.log("Obtained target clickable elements:");
  //console.log(targetEls);
  //if (targetEls && targetEls.length >= 2) {
  //targetEls[1].click();
  //};
  /** @type {DOMRect} */
  let currEl;
  if (targetEls) {
    extras.push(`targetEls: ${targetEls}`);
    targetEls.forEach((el) => {
      currEl = el.getBoundingClientRect();
      if (currEl.width > 100 && currEl.height > 100) {
        extras.push(`Big enough element: ${el}`);
        el.click();
        autobots.sleep(100);
        console.log(extras);
        return;
      }
    });
  }
  console.log(extras);
};


/**
 * @file shortcuts.js
 * @description Defines custom keyboard shortcuts for SurfingKeys.
 *
 * Surfingkeys basic mapping function has the following formatting
 *
 * The shortcuts objects defined here are literally injected as written to surfingkeys
 * `options.html` (as well as everything in this script), as the last loaded script of it.
 *
 * Shortcuts objects have the following format:
 *
 * @const shortcuts.global
 * @description Global keymaps, that will be configured to all website urls, being each item
 * of it one shortcut, and containing the following elements:
 * @field {str} key - Key combination to use this shortcut.
 * @field {function} command - Function that will be executed in this shorcut
 * @field {str} category - Category name from the available ones in `utils.categories`, used to
 * group the shortcut, for example in the usage popup (toggled with ?)
 * @field {str} description - Description of the shortcut
 * @see utils:utils.categories
 *
 * @example
 * utils.dispatchSKEvent("front", ["addCommand", "duteste", "teste description"]);
 */

const shortcuts = {};

shortcuts.global = [
  {
    key: "/",
    category: "misc",
    description: "Find in current page",
    command: () => {
      utils.dispatchSKEvent("front", ["openFinder"]);
    },
  },
  {
    key: "<Space>W",
    category: "mouseClick",
    description: "Test toggle mouse",
    command: () => {
      api.RUNTIME("toggleMouseQuery", {});
    },
  },
  {
    key: "<Space>br",
    category: "sessions",
    description: "Remove bookmark",
    command: () => {
      api.RUNTIME("removeBookmark");
    },
  },
  {
    key: "<Space>X",
    category: "misc",
    description: "Passthrough 1 sec",
    command: () => {
      api.Normal.passThrough(1000);
    },
  },
  {
    key: "<Space>ab",
    category: "sessions",
    description: "Add bookmark",
    command: () => {
      const page = {
        url: window.location.href,
        title: document.title,
      };
      api.Front.openOmnibar({ type: "AddBookmark", extra: page });
    },
  },
  {
    key: "ye",
    command: commands.editClipboard,
    category: "clipboard",
    description: "Edit clipboard and yank",
  },
  {
    key: "yl",
    category: "clipboard",
    description: "Yank links",
    command: commands.copyLinks,
  },
  {
    key: "yL",
    category: "clipboard",
    description: "Copy multiple link URLs to the clipboard",
    command: commands.copyMultipleLinks,
  },
  {
    key: "yc",
    category: "clipboard",
    description: "Yank closest code block",
    command: commands.copyCodeBlock,
  },
  {
    key: "yu",
    category: "clipboard",
    description: "Copy URL path of current page",
    command: () => {
      api.Clipboard.write(window.location.href);
    },
  },
  {
    key: "yX",
    category: "clipboard",
    description: "Clean current clipboard.",
    command: () => {
      api.Clipboard.write("");
      api.Front.showBanner("Clipboard cleaned.", 1000);
    },
  },
  {
    key: "yC",
    category: "clipboard",
    description: "Hint code blocks to copy",
    command: () => {
      utils.createHints(utils.codeBlockHints);
    },
  },
  {
    key: "yy",
    category: "clipboard",
    description: "Yank current url",
    command: () => {
      api.Clipboard.write(`${window.location.href}`);
      api.Front.showBanner(`Yanked ${window.location.href}`);
    },
  },
  {
    key: "yY",
    category: "clipboard",
    description: "Append current url to existing clipboard content.",
    command: () => {
      api.Clipboard.read((c) => {
        api.Clipboard.write([`${window.location.href}`, `${c.data}`].join("\n"));
      });
    },
  },
  {
    key: "yU",
    command: commands.openMultipleYankURL,
    category: "clipboard",
    description: "Go to multiple yanked URLs",
  },
  {
    key: "<Space>xx",
    category: "tabs",
    description: "Close tab",
    command: () => {
      api.RUNTIME("closeTab");
    },
  },
  {
    key: "<Space>x[",
    category: "tabs",
    description: "Close tab on left",
    command: () => {
      api.RUNTIME("CloseTabLeft");
    },
  },
  {
    key: "<Space>x]",
    category: "tabs",
    description: "Close tab on right",
    command: () => {
      api.RUNTIME("CloseTabRight");
    },
  },
  {
    key: "<Space>x}",
    category: "tabs",
    description: "Close all tabs to right",
    command: () => {
      commands.closeTabsDirection("right");
    },
  },
  {
    key: "<Space>x{",
    category: "tabs",
    description: "Close all tabs to left",
    command: () => {
      commands.closeTabsDirection("left");
    },
  },
  {
    key: ";pv",
    command: commands.togglePdfViewer,
    category: "settings",
    description: "Toggle PDF viewer from SurfingKeys",
  },
  {
    key: "<Space>di",
    category: "misc",
    description: "Download image",
    command: () => {
      api.Hints.create("img", (element) => {
        if (
          element instanceof HTMLImageElement ||
          element instanceof HTMLSourceElement ||
          element instanceof HTMLTrackElement ||
          element instanceof HTMLIFrameElement ||
          element instanceof HTMLEmbedElement
        ) {
          api.RUNTIME("download", {
            url: element.src,
          });
        }
      });
    },
  },
  {
    key: "<Space>oe",
    command: commands.editOpenLink,
    category: "misc",
    description: "Vi edit open link",
  },
  {
    key: "<Space>O",
    category: "misc",
    description: "Edit current url and open",
    command: commands.editAndGoToUrl,
  },
  {
    key: "<Space>R",
    category: "pageNav",
    description: "Reload page",
    command: () => {
      api.RUNTIME("reloadTab", { nocache: false });
    },
  },

  {
    key: "<Space>tr",
    category: "tabs",
    description: "Restore last closed tab",
    command: () => api.RUNTIME("openLast"),
  },
  {
    key: "<Space>tR",
    category: "tabs",
    description: "Focus random tab",
    command: () => commands.focusRandomTab,
  },
  {
    key: "<Space>tc",
    category: "tabs",
    description: "Show total number of tabs",
    command: commands.countTabs,
  },
  {
    key: "F",
    category: "mouseClick",
    description: "Multiple hints main click",
    command: () => {
      utils.createHints(
        "*",
        (el) => {
          el.dispatchEvent(utils.mouseClick);
        },
        {
          tabbed: true,
          active: false,
          multipleHits: true,
        }
      );
    },
  },
  {
    key: "<Ctrl-Space>",
    category: "mouseClick",
    description: "Main click",
    command: () => {
      utils.createHints(utils.mainHints);
    },
  },
  {
    key: "<Alt-Space>",
    category: "mouseClick",
    description: "Hold click",
    command: () => {
      utils.createHints(
        utils.mainHints,
        (el) => {
          el.dispatchEvent(utils.mouseHold);
        },
        {
          tabbed: false,
          active: true,
          multipleHits: false,
        }
      );
    },
  },
  {
    key: "<Space>ol",
    category: "mouseClick",
    description: "Multiple inactive tabs",
    command: () => {
      utils.createHints("", api.Hints.dispatchMouseClick, {
        multipleHits: true,
        active: false,
        tabbed: true,
      });
    },
  },
  {
    key: "<Space>L",
    category: "mouseClick",
    description: "Left click hint elements",
    command: () => {
      utils.createHints(
        "*",
        (el) => {
          el.focus;
          el.dispatchEvent(utils.mouseLeft);
        },
        {
          tabbed: false,
          active: true,
          multipleHits: false,
        }
      );
    },
  },
  {
    key: "<Space>oL",
    category: "mouseClick",
    description: "Multiple inactive tabs",
    command: () => {
      utils.createHints("", api.Hints.dispatchMouseClick, {
        multipleHits: true,
        active: false,
        tabbed: true,
      });
    },
  },
  {
    key: "<Ctrl-j>",
    category: "mouseClick",
    description: "Mouse Over Elements",
    command: commands.mouseOver,
  },
  {
    key: "<Space>B",
    category: "mouseClick",
    description: "Hint buttons",
    command: () => {
      utils.createHints(utils.buttonHints, api.Hints.dispatchMouseClick, {
        multipleHits: false,
        tabbed: false,
        active: true,
      });
    },
  },
  {
    key: "<Space>0",
    category: "settings",
    description: "Toggle surfingkeys",
    command: () => {
      api.RUNTIME("toggleBlocklist");
    },
  },
  {
    key: "<Space><Ctrl-Space>",
    category: "omnibar",
    description: "Main omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "URLs", tabbed: false });
    },
  },
  {
    key: "<Space><Space>]",
    category: "omnibar",
    description: "Omnibar headings",
    command: commands.omniHeads,
  },
  {
    key: "<Space><Space>E",
    category: "omnibar",
    description: "Omnibar alternatives urls / extensions",
    command: commands.omniAltUrls,
  },
  {
    key: "<Space><Space>h",
    description: "Omni history",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({
        type: "History",
        tabbed: false,
        extra: { prompt: " " },
      });
    },
  },
  {
    key: "<Space><Space>H",
    description: "Omni history tabbed",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({
        type: "History",
        tabbed: true,
        extra: {
          prompt: " ",
        },
      });
    },
  },
  {
    key: "<Space><Space>t",
    description: "Omni tabs",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "Tabs" });
    },
  },
  {
    key: "<Space><Space>b",
    description: "Omni bookmarks",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({
        type: "Bookmarks",
        tabbed: false,
        extra: {
          onInput: " ",
        },
      });
    },
  },
  {
    key: "<Space><Space>B",
    description: "Omni bookmarks tabbed",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({
        type: "Bookmarks",
        tabbed: true,
        extra: {
          prompt: " ",
        },
      });
    },
  },
  {
    key: "<Space><Space>:",
    description: "Omni Commands",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "Commands" });
    },
  },
  {
    key: "<Space><Space>w",
    description: "Omni windows",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "Windows" });
    },
  },
  {
    key: "<Space><Space>T",
    description: "Omni history tabs",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "TabURLs" });
    },
  },
  {
    key: "<Space><Space>u",
    description: "Omni open url",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({
        type: "URLs",
        tabbed: false,
      });
    },
  },
  {
    key: "<Space><Space>s",
    description: "Omni search engine",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "SearchEngine" });
    },
  },
  {
    key: "<Space><Space>q",
    description: "Omni query",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "OmniQuery" });
    },
  },
  {
    key: "<Space><Space>u",
    description: "Omni user URLs",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "UserURLs" });
    },
  },
  {
    key: "<Space><Space>v",
    description: "Omni vi marks",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "VIMarks" });
    },
  },
  {
    key: "<Space><Space>r",
    description: "Omni recently closed",
    category: "omnibar",
    command: () => {
      api.Front.openOmnibar({ type: "RecentlyClosed" });
    },
  },
  {
    key: "<Space>l",
    category: "pageNav",
    description: "Next page",
    command: () => commands.changePage("up"),
  },
  {
    key: "<Space>h",
    category: "pageNav",
    description: "Prev page",
    command: () => commands.changePage("down"),
  },
  {
    key: "]]",
    category: "pageNav",
    description: "1 page forward history",
    command: () => history.forward(),
  },
  {
    key: "[[",
    category: "pageNav",
    description: "1 page backward history",
    command: () => history.back(),
  },
  {
    key: "g.",
    category: "pageNav",
    description: "Go to parent domain",
    command: () => {
      const subdomains = window.location.host.split(".");
      const parentDomain = (subdomains.length > 2 ? subdomains.slice(1) : subdomains).join(".");
      commands.openLink(`${window.location.protocol}//${parentDomain}`);
    },
  },
  {
    key: "<Ctrl-d>",
    category: "scroll",
    description: "Scroll down",
    command: () => api.Normal.scroll("pageDown"),
  },
  {
    key: "<Ctrl-u>",
    category: "scroll",
    description: "Scroll up",
    command: () => api.Normal.scroll("pageUp"),
  },
  {
    key: ";r",
    category: "scroll",
    description: "Reset scroll",
    command: utils.resetScrollTarget,
  },
  {
    key: ";;",
    category: "scroll",
    description: "Focus hints",
    command: utils.focusScrollTarget,
  },
  {
    key: "w",
    category: "scroll",
    description: "Focus hints",
    command: utils.focusScrollTarget,
  },
  {
    key: "W",
    category: "scroll",
    description: "Rest scroll",
    command: utils.resetScrollTarget,
  },
  {
    key: "gg",
    category: "scroll",
    description: "Scroll to beginnign of page.",
    command: () => {
      api.Normal.scroll("top");
    },
  },
  {
    key: "G",
    category: "scroll",
    description: "Scroll to bottom of page.",
    command: () => {
      api.Normal.scroll("bottom");
    },
  },
  {
    key: "<Ctrl-e>",
    category: "scroll",
    description: "Scroll left",
    command: () => {
      api.Normal.scroll("left");
    },
  },
  {
    key: "<Ctrl-E>",
    category: "scroll",
    description: "Scroll leftmost",
    command: () => {
      api.Normal.scroll("leftmost");
    },
  },
  {
    key: "<Ctrl-f>",
    category: "scroll",
    description: "Scroll right",
    command: () => {
      api.Normal.scroll("right");
    },
  },
  {
    key: "<Ctrl-F>",
    category: "scroll",
    description: "Scroll rightmost",
    command: () => {
      api.Normal.scroll("rightmost");
    },
  },
  {
    key: "<Space>ob",
    category: "sessions",
    description: "Search bookmarks",
    command: () => {
      api.RUNTIME("openBookmark");
    },
  },
  {
    key: "<Space>Sr",
    category: "tabs",
    description: "Restore session",
    command: () => {
      api.RUNTIME("openSession", {
        name: "LAST",
      });
    },
  },
  {
    key: "<Space>SX",
    category: "tabs",
    description: "Save session + quit",
    command: () => {
      api.RUNTIME("createSession", {
        name: "LAST",
        quitAfterSaved: true,
      });
    },
  },
  {
    key: "<Space>nt",
    category: "tabs",
    description: "Open new tab",
    command: () => {
      api.RUNTIME("openLink", {
        tab: { tabbed: true, active: true },
        url: "about:blank",
      });
    },
  },
  {
    key: "<Space>np",
    category: "tabs",
    description: "Incognito tab",
    command: () => {
      api.RUNTIME("openIncognito", { url: window.location.href });
    },
  },
  {
    key: "<Space>td",
    category: "tabs",
    description: "Duplicate tab",
    command: () => {
      api.RUNTIME("duplicateTab");
    },
  },
  {
    key: "<Space>tD",
    category: "tabs",
    description: "Duplicate current tab non-activelly",
    command: () => {
      commands.openLink(window.location.href, { newTab: true, active: false });
    },
  },
  {
    key: "<Space>tu",
    category: "tabs",
    description: "Ungroup tabs",
    command: () => {
      api.RUNTIME("ungroupTab");
    },
  },
  {
    key: "<Space>tx",
    category: "tabs",
    description: "Collapse tab group",
    command: () => {
      api.RUNTIME("collapseGroup");
    },
  },
  {
    key: "<Space>tg",
    category: "tabs",
    description: "Create tab group",
    command: () => {
      api.RUNTIME("createTabGroup");
    },
  },
  {
    key: "]T",
    category: "tabs",
    description: "Go to last right tab",
    command: () => {
      commands.goToTab("l");
    },
  },
  {
    key: "[T",
    category: "tabs",
    description: "Go to first left tab",
    command: () => {
      commands.goToTab("f");
    },
  },
  {
    key: "<Space>tp",
    category: "tabs",
    description: "Pin current tab",
    command: () => {
      api.RUNTIME("togglePinTab");
    },
  },
  // @TODO: Check chooseTab exists on public api
  {
    key: "<Space>T",
    category: "tabs",
    description: "Select tab",
    command: () => {
      api.Front.chooseTab();
    },
  },
  {
    key: "<Space>tw",
    category: "tabs",
    description: "Move tab to new window",
    command: () => {
      api.RUNTIME("moveToWindow", {
        windowId: -1,
      });
    },
  },
  {
    key: "<Space>t]",
    category: "tabs",
    description: "Move tab forward",
    command: () => {
      api.RUNTIME("moveTab", {
        step: 1,
      });
    },
  },
  {
    key: "<Space>t[",
    category: "tabs",
    description: "Move tab backward",
    command: () => {
      api.RUNTIME("moveTab", {
        step: -1,
      });
    },
  },
  {
    key: "<Space>t{",
    category: "tabs",
    description: "Move tab to start",
    command: () => {
      api.RUNTIME("moveTab", {
        step: -100,
      });
    },
  },
  {
    key: "<Space>t}",
    category: "tabs",
    description: "Move tab to end",
    command: () => {
      api.RUNTIME("moveTab", {
        step: 100,
      });
    },
  },
  {
    key: "]t",
    category: "tabs",
    description: "Next tab",
    command: () => {
      api.RUNTIME("nextTab");
    },
  },
  {
    key: "[t",
    category: "tabs",
    description: "Prev tab",
    command: () => {
      api.RUNTIME("previousTab");
    },
  },
  {
    key: "[r",
    category: "tabs",
    description: "Last activated tab",
    command: () => {
      api.RUNTIME("goToLastTab");
    },
  },
  {
    key: "<Space>ty",
    category: "tabs",
    description: "Go to playing tab",
    command: commands.focusPlayingTab,
  },
  {
    key: "p",
    category: "misc",
    description: "Play closest video",
    command: commands.togglePlayVideo,
  },
  {
    key: "<Space>-",
    category: "misc",
    description: "Raise video volume 10%",
    command: () => commands.changeVolume(0.1),
  },
  {
    key: "<Space>+",
    category: "misc",
    description: "Lower video volumne 10%",
    command: () => commands.changeVolume(-0.1),
  },
  {
    key: "}",
    category: "misc",
    description: "Video forward",
    command: commands.videoForward,
  },
  {
    key: "{",
    category: "misc",
    description: "Video backward",
    command: commands.videoBackward,
  },
  {
    key: "<Space>F",
    category: "misc",
    description: "Toggle fullscreen video",
    command: commands.toggleFullScreenVideo,
  },
  {
    key: "<Space>tm",
    category: "tabs",
    description: "Mute tab",
    command: () => {
      api.RUNTIME("muteTab");
    },
  },
  {
    key: "y}",
    category: "tabs",
    description: "yank right tabs url to clipboard",
    command: () => {
      commands.yankTabsDirection();
    },
  },
  {
    key: "y{",
    category: "tabs",
    description: "yank left tabs url to clipboard",
    command: () => {
      commands.yankTabsDirection("left");
    },
  },
  {
    key: "yV",
    category: "misc",
    description: "Yank closest video source",
    command: commands.yankVideoSrc,
  },
  {
    key: "<Space>tG",
    category: "tabs",
    description: "Gather tabs in one window",
    command: () => {
      api.RUNTIME("gatherWindows");
    },
  },
  {
    key: "<Space>tF",
    category: "tabs",
    description: "Gather filtered tabs in one window",
    command: () => {
      api.Front.openOmnibar({
        type: "Tabs",
        extra: {
          action: "gather",
        },
      });
    },
  },
  {
    key: "<Space>vT",
    description: "Set video time",
    command: commands.setVideoTime,
  },
  {
    key: "<",
    description: "- volume",
    command: () => {
      commands.changeVolume(-0.1);
    },
  },
  {
    key: ">",
    description: "+ volume",
    command: () => {
      commands.changeVolume(0.1);
    },
  },
  {
    key: "<Space>va",
    description: "Download current nearest video",
    command: commands.downloadVideoAutomatic,
  },
  {
    key: "<Space>vd",
    group: "misc",
    description: "Download hinted video",
    command: () => {
      commands.downloadHintVideo();
    },
  },
  // @TODO: Check if addVIMark  is available on public api
  {
    key: "<Space>ma",
    category: "vimMarks",
    description: "Add vi mark",
    command: () => {
      api.Normal.addVIMark();
    },
  },
  {
    key: "<Space>mg",
    category: "vimMarks",
    description: "Jump to vi mark",
    command: () => {
      api.Normal.jumpVIMark();
    },
  },
  {
    key: "<Space>vo",
    category: "misc",
    description: "Toggle video control bar",
    command: commands.toggleControlBar,
  },
  {
    key: "<Space>vO",
    category: "misc",
    description: "Video show time",
    command: commands.videoShowTime,
  },
  {
    key: "M",
    category: "misc",
    description: "Toggle mute video",
    command: commands.toggleMuteVideo,
  },
  {
    key: "<Space>v1",
    description: "Set video to 10%",
    command: () => {
      commands.setVideoTime(0.1);
    },
  },
  {
    key: "<Space>v2",
    description: "Set video to 20%",
    command: () => {
      commands.setVideoTime(0.2);
    },
  },
  {
    key: "<Space>v3",
    description: "Set video to 30%",
    command: () => {
      commands.setVideoTime(0.3);
    },
  },
  {
    key: "<Space>v4",
    description: "Set video to 40%",
    command: () => {
      commands.setVideoTime(0.4);
    },
  },
  {
    key: "<Space>v5",
    description: "Set video to half",
    command: () => {
      commands.setVideoTime(0.5);
    },
  },
  {
    key: "<Space>v6",
    description: "Set video to 60%",
    command: () => {
      commands.setVideoTime(0.6);
    },
  },
  {
    key: "<Space>v7",
    description: "Set video to 70%",
    command: () => {
      commands.setVideoTime(0.7);
    },
  },
  {
    key: "<Space>v8",
    description: "Set video to 80%",
    command: () => {
      commands.setVideoTime(0.8);
    },
  },
  {
    key: "<Space>v9",
    description: "Set video to 90%",
    command: () => {
      commands.setVideoTime(0.9);
    },
  },
  {
    key: "<Space>vp",
    category: "misc",
    description: "Click video to play",
    command: commands.clickVideoPlay,
  },
  {
    key: "<Space>j",
    category: "misc",
    description: "Preview over a video thumbnail",
    command: commands.startVideoPreviewHints,
  },
  {
    key: "<Space>J",
    category: "misc",
    description: "Stop preview over a video",
    command: commands.stopAllVideoPreviews,
  },
  {
    key: "<Space>P",
    category: "misc",
    description: "Preview image in a floating overiew from link",
    command: () => {
      utils.createHints("a[href]", (a) => {
        commands.previewHTML(a.href);
      });
    },
  },
  {
    key: "zr",
    category: "pageNav",
    description: "Zoom reset",
    command: () => {
      api.RUNTIME("setZoom", {
        zoomFactor: 0,
      });
    },
  },
  {
    key: "zi",
    category: "pageNav",
    description: "Zoom in",
    command: () => {
      api.RUNTIME("setZoom", {
        zoomFactor: 0.1,
      });
    },
  },
  {
    key: "zo",
    category: "pageNav",
    description: "Zoom out",
    command: () => {
      api.RUNTIME("setZoom", {
        zoomFactor: -0.1,
      });
    },
  },
  {
    key: "<Space>kH",
    category: "misc",
    description: "Debug get clickable elements",
    command: autobots.clickreddit,
  },
  {
    key: "<Space>kf",
    category: "misc",
    description: "Debug flutter",
    command: () => {
      autobots.findFlutterVideoGridPoints(2, 2, 1000, false);
    },
  },
  {
    key: "<Space>kF",
    category: "misc",
    description: "Debug flutter",
    command: () => {
      autobots.findFlutterVideoGridPoints(2, 4, 2000, true);
    },
  },
  {
    key: "<Space>kh",
    category: "misc",
    description: "Debug input create hints",
    command: commands.debugInputCreateHints,
  },
  {
    key: "<Space>ks",
    category: "misc",
    description: "Run given skevent",
    command: commands.debugInputSKEvent,
  },
  {
    key: "<Space>ki",
    category: "misc",
    description: "Debug run input runtime",
    command: commands.debugInputRuntime,
  },
  {
    key: "<Space>kS",
    category: "misc",
    description: "Debug run sk function (api/utils/commands) with input",
    command: commands.debugRunSkFn,
  },
  {
    key: "<Space>kO",
    category: "misc",
    description: "Debug run omnibar",
    command: () => {},
  },
  {
    key: "<Space>ko",
    category: "misc",
    description: "Debug run omnibar",
    command: () => {
      utils.dispatchSKEvent("front", ["addCommand", "duteste", "teste description"]);
      const _open = api.Front.openOmnibar;
      api.Front.openOmnibar = function (args) {
        const aaa = document.querySelectorAll("#sk_omnibar");
        console.log(aaa);
        api.Normal.feedkeys("a");
        return _open.call(this, args);
      };
      api.Front.openOmnibar({ type: "Commands" });
    },
  },
  // @TODO: find to which specific site i created this single key like/next shortcuts.
  {
    key: "L",
    category: "misc",
    description: "Like",
    command: () => {
      const likeBtn = utils.findElementByPartialMatch("button", "like");
      if (likeBtn !== null) {
        likeBtn?.click();
      }
    },
  },
  {
    key: "K",
    category: "misc",
    description: "Previous",
    command: () => {
      const prevBtn = utils.findElementByPartialMatch("button", "previous");
      if (prevBtn !== null) {
        prevBtn?.click();
      }
    },
  },
  {
    key: "J",
    category: "misc",
    description: "Next",
    command: () => {
      const nextBtn = utils.findElementByPartialMatch("button", "next");
      if (nextBtn !== null) {
        nextBtn?.click();
      }
    },
  },
  {
    key: "<Space>kA",
    category: "omnibar",
    description: "Debug run llm gpt",
    command: async () => {
      const vid = utils.findClosestEl("video");
      console.log(vid);
      if (vid instanceof HTMLVideoElement) {
        vid.play();
        return vid;
      }
      const tsts = utils.findClosestEl("shreddit-post");
      console.log(tsts);
      if (tsts) {
        commands.dispatchRightClick(tsts);
        return tsts;
      }
    },
  },
];

shortcuts.sites = [
  {
    domain: /deezer\.com/i,
    mappings: [
      {
        key: "p",
        category: "misc",
        description: "Play/Pause",
        command: commands.testDeezer,
        leader: false,
      },
    ],
  },
  {
    domain: /github\.com/i,
    mappings: [
      {
        key: "c",
        category: "misc",
        description: "Copy git http repo clone command",
        command: () => {
          commands.cloneGitAddress("http");
        },
      },
      {
        key: "C",
        category: "misc",
        description: "Copy git ssh repo clone command",
        command: () => {
          commands.cloneGitAddress("ssh");
        },
      },
      {
        key: "s",
        category: "misc",
        description: "Star git repo",
        command: commands.clickStarButton,
      },
      {
        key: "r",
        category: "misc",
        description: "Yank author/repo",
        command: commands.yankGitAuthorAndRepo,
      },
      {
        key: "i",
        category: "misc",
        description: "Go to issues",
        command: commands.gitGoToIssues,
      },
    ],
  },
  {
    domain: /gitlab\.gnome\.org/i,
    mappings: [
      {
        key: "c",
        category: "misc",
        description: "Copy git http repo clone command",
        command: () => {
          commands.cloneGitLabGnomeAddress("http");
        },
      },
      {
        key: "C",
        category: "misc",
        description: "Copy git ssh repo clone command",
        command: () => {
          commands.cloneGitLabGnomeAddress("ssh");
        },
      },
    ],
  },
  {
    domain: /google\.com/i,
    mappings: [
      {
        key: "l",
        category: "misc",
        description: "Next page",
        command: commands.googleNextPage,
      },
      {
        key: "h",
        category: "misc",
        description: "Prev page",
        command: commands.googlePrevPage,
      },
    ],
  },
  {
    domain: /app\.timfun\.com\.br/i,
    mappings: [
      {
        key: "p",
        category: "misc",
        description: "Play fitst timfun video",
        leader: false,
        command: () => {
          autobots.flutterClickAt({ rx: 457, ry: 364 });
        },
      },
    ],
  },
  {
    domain: /reddit\.com/i,
    mappings: [
      {
        key: "l",
        category: "misc",
        description: "Like video",
        command: commands.redditLike,
      },
      {
        key: "c",
        category: "misc",
        description: "Open Comments",
        command: commands.redditComments,
      },
      {
        key: "P",
        category: "misc",
        description: "Play video",
        command: commands.redditPlayButton,
        leader: false,
      },
      {
        key: "z",
        category: "misc",
        description: "Fold Comment",
        command: commands.redditFold,
      },
      {
        key: "n",
        category: "misc",
        description: "Next Carrousel",
        command: () => {
          commands.redditNavCarr("next");
        },
      },
      {
        key: "p",
        category: "misc",
        description: "Prev Carrousel",
        command: () => {
          commands.redditNavCarr("prev");
        },
      },
    ],
  },
  {
    domain: /youtube\.com/i,
    mappings: [
      {
        key: "l",
        category: "misc",
        description: "Like video",
        command: commands.likeYtVideo,
      },
    ],
  },
];


/**
 * @file alt_modes_shortcuts.js
 * @description Defines SurfingKeys shortcuts to command mode (omnibar), insert maps, and ace maps.
 *
 */

const command_shortcuts = {};

command_shortcuts.mappings = [
  {
    alias: "<Ctrl-j>",
    map: "<Tab>",
    annot: "Backward cicle through candidates",
  },
  {
    alias: "<Ctrl-k>",
    map: "<Shift-Tab>",
    annot: "Forward cicle through candidates",
  },
  {
    alias: "<Ctrl-n>",
    map: "<Ctrl-.>",
    annot: "Show next page results",
  },
  {
    alias: "<Ctrl-p>",
    map: "<Ctrl-,>",
    annot: "Show previous page results",
  },
  {
    alias: "<Ctrl-y>",
    map: "<Ctrl-c>",
    annot: "Copy item",
  },
  {
    alias: "<Ctrl-x>",
    map: "<Shift-Enter>",
    annot: "Open selected item in current tab and close omnibar",
  },
  {
    alias: "<Ctrl-t>",
    map: "<Ctrl-Enter>",
    annot: "Open omnibar item without closing it",
  },
  {
    alias: "<Ctrl-e>",
    map: "<Ctrl-i>",
    annot: "Edit selected URL with vim editor, then open",
  },
];

const acemaps = {};

acemaps.mappings = [
  {
    alias: "<A-l>",
    map: "<end>",
    mode: "normal",
    annot: "Line end",
  },
  {
    alias: "<A-l>",
    map: "<end>",
    mode: "insert",
    annot: "Line end",
  },
  {
    alias: "<A-l>",
    map: "<end>",
    mode: "visual",
    annot: "Line end",
  },
  {
    alias: "<A-l>",
    map: "<end>",
    mode: "visual",
    annot: "Line end",
  },
  {
    alias: "<A-h>",
    map: "<home>",
    mode: "normal",
    annot: "Line beginning",
  },
  {
    alias: "<A-h>",
    map: "<home>",
    mode: "insert",
    annot: "Line beginning",
  },
  {
    alias: "<A-h>",
    map: "<home>",
    mode: "caret",
    annot: "Line beginning",
  },
  {
    alias: "<A-h>",
    map: "<home>",
    mode: "caret",
    annot: "Line beginning",
  },
  {
    alias: "jk",
    map: "<Esc>",
    mode: "insert",
    annot: "Esc",
  },
  {
    alias: "kj",
    map: "<Esc>",
    mode: "insert",
    annot: "Esc",
  },
  {
    alias: "n",
    map: "o",
    mode: "normal",
    annot: "New line",
  },
  {
    alias: "<C-x>",
    map: "<Esc>:wq",
    mode: "normal",
    annot: "Quit editor",
  },
];

utils.registerAltShortcuts();


/**
 * @file theme.js
 * @description Defines theme colors to surfingkeys hints, cursor, marks.
 *
 * Themes are defined in `theme.colorSchemes` objects, that are a css string, containing the
 * following variables defined:
 *   - --font - Ex: (like 'Source Code Pro', Ubuntu, sans)
 *   - --font-size - Ex: 12
 *   - --banner-font-size - sk_banner Front popup elements font size. Ex: 12px
 *   - --font-weight {string} - Ex: bold
 *   - --fg {string} - html_color
 *   - --bg {string} - html_color
 *   - --bg-dark {string} - html_color
 *   - --border {string} - html_color
 *   - --main-fg {string} - html_color
 *   - --accent-fg {string} - html_color
 *   - --info-fg {string} - html_color
 *   - --select
 *   - Colors (orange|red|yellow|cyan|violet|blue)
 *
 */

const theme = {};

theme.hints = {};

theme.visual = {};

/*=============
  Visual Themes
  =============*/

/*--
  Du
  --*/

theme.visual.du = [
  {
    type: "cursor",
    background_color: "#2E5164",
    color: "#FFFFFF",
  },
  {
    type: "marks",
    background_color: "#7EF5BF99",
    color: "#000000",
  },
];

/*-------
  Dracula
  -------*/

theme.visual.dracula = [
  {
    type: "cursor",
    background_color: "#44475A",
    color: "#8BE9FD",
  },
  {
    type: "marks",
    background_color: "#282A36",
    color: "#BD93F9",
  },
];

/*--------------
  Tomorrow Night
  --------------*/

theme.visual.tomorrowNight = [
  {
    type: "cursor",
    background_color: "#81A2BE",
    color: "#1D1F21",
  },
  {
    type: "marks",
    background_color: "#52C19699",
    color: "#1D1F21",
  },
];

/*----
  Nord
  ----*/

theme.visual.nord = [
  {
    type: "cursor",
    background_color: "#88C0D0",
    color: "#2E3440",
  },
  {
    type: "marks",
    background_color: "#A3BE8C99",
    color: "#2E3440",
  },
];

/*--------
  Doom One
  --------*/

theme.visual.doomOne = [
  {
    type: "cursor",
    background_color: "#51AFEF",
    color: "#21242B",
  },
  {
    type: "marks",
    background_color: "#98BE6599",
    color: "#21242B",
  },
];

/*-------
  Monokai
  -------*/

theme.visual.monokai = [
  {
    type: "cursor",
    background_color: "#F92660",
    color: "#1D1E19",
  },
  {
    type: "marks",
    background_color: "#A6E22E99",
    color: "#1D1E19",
  },
];

/*--------
  rosePine
  --------*/

theme.visual.rosePine = [
  {
    type: "cursor",
    background_color: "#C4A7E7",
    color: "#191724",
  },
  {
    type: "marks",
    background_color: "#9CCFD8",
    color: "#191724",
  },
];

/*------------
  rosePineMoon
  ------------*/

theme.visual.rosePineMoon = [
  {
    type: "cursor",
    background_color: "#C4A7E7",
    color: "#232136",
  },
  {
    type: "marks",
    background_color: "#9CCFD8",
    color: "#232136",
  },
];

/*=============
  Color Schemes
  =============*/

/*-------
  Du
  -------*/

theme.hints.du = [
  {
    type: "text",
    background_color: "#000000",
    color: "#F55069",
    border_size: "4px",
    border_color: "#262034",
    background: "none",
    font_size: "16px",
    begin_color: "#EC64E5",
    begin_background_color: "#000000",
    font_family: '"FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue"',
  },
  {
    type: "main",
    background_color: "#A7A7A7",
    color: "#581EEC",
    border_size: "4px",
    border_color: "#8566EC",
    background: "none",
    font_size: "16px",
    font_family: '"FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue"',
  },
];

/*-------
  Dracula
  -------*/

theme.hints.dracula = [
  {
    type: "text",
    background_color: "#282A36",
    color: "#FF79C6",
    border_size: "4px",
    border_color: "#6272A4",
    background: "none",
    font_size: "16px",
    begin_color: "#BD93F9",
    begin_background_color: "#191A21",
    font_family: '"FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue"',
  },
  {
    type: "main",
    background_color: "#21222C",
    color: "#F1FA8C",
    border_size: "4px",
    border_color: "#50FA7B",
    background: "none",
    font_size: "16px",
    font_family: '"FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue"',
  },
];

/*--------------
  Tomorrow Night
  --------------*/

theme.hints.tomorrowNight = [
  {
    type: "text",
    background_color: "#1D1F21",
    color: "#C5C8C6",
    border_size: "solid 2px",
    border_color: "#373B41",
    background: "none",
    font_size: "13px",
  },
  {
    type: "main",
    background_color: "#1D1F21",
    color: "#52C196",
    border_size: "solid 2px",
    border_color: "#373B41",
    background: "none",
    font_size: "15px",
  },
];

/*----
  Nord
  ----*/

theme.hints.nord = [
  {
    type: "text",
    background_color: "#3B4252",
    color: "#E5E9F0",
    border_size: "solid 2px",
    border_color: "#4C566A",
    background: "none",
    font_size: "13px",
  },
  {
    type: "main",
    background_color: "#3B4252",
    color: "#A3BE8C",
    border_size: "solid 2px",
    border_color: "#4C566A",
    background: "none",
    font_size: "15px",
  },
];

/*--------
  Doom One
  --------*/

theme.hints.doomOne = [
  {
    type: "text",
    background_color: "#2E3440",
    color: "#51AFEF",
    border_size: "solid 2px",
    border_color: "#282C34",
    background: "none",
    font_size: "13px",
  },
  {
    type: "main",
    background_color: "#2E3440",
    color: "#98BE65",
    border_size: "4px",
    border_color: "#282C34",
    background: "none",
    font_size: "15px",
  },
];

/*-------
  Monokai
  -------*/

theme.hints.monokai = [
  {
    type: "text",
    background_color: "#272822",
    color: "#A6E2EE",
    border_size: "solid 2px",
    border_color: "#2D2E2E",
    background: "none",
    font_size: "13px",
  },
  {
    type: "main",
    background_color: "#272822",
    color: "#F92660",
    border_size: "solid 2px",
    border_color: "#2D2E2E",
    background: "none",
    font_size: "15px",
  },
];

/*-----------
  Rose Pine
-----------*/

theme.hints.rosePine = [
  {
    type: "text",
    background_color: "#191724",
    color: "#E0DEF4",
    border_size: "0px",
    border_color: "#191724",
    background: "#191724",
    font_size: "13pt",
    font_family:
      "'JetBrains Mono NL', 'Cascadia Code', 'Helvetica Neue', Helvetica, Arial, sans-serif",
  },
  {
    type: "main",
    background_color: "#191724",
    color: "#E0DEF4",
    border_size: "0px",
    border_color: "#191724",
    background: "#191724",
    font_size: "13pt",
    font_family:
      "'JetBrains Mono NL', 'Cascadia Code', 'Helvetica Neue', Helvetica, Arial, sans-serif",
  },
];

theme.hints.rosePineMoon = [
  {
    type: "text",
    background_color: "#232136",
    color: "#E0DEF4",
    border_size: "0px",
    border_color: "#232136",
    background: "#232136",
    font_size: "13pt",
    font_family:
      "'JetBrains Mono NL', 'Cascadia Code', 'Helvetica Neue', Helvetica, Arial, sans-serif",
  },
  {
    type: "main",
    background_color: "#232136",
    color: "#E0DEF4",
    border_size: "0px",
    border_color: "#232136",
    background: "#232136",
    font_size: "13pt",
    font_family:
      "'JetBrains Mono NL', 'Cascadia Code', 'Helvetica Neue', Helvetica, Arial, sans-serif",
  },
];

theme.generic = `
.sk_theme {
  background: var(--bg);
  color: var(--fg);
  background-color: var(--bg);
  border-color: var(--border);
  font-family: var(--font);
  font-size: var(--font-size);
  font-weight: var(--font-weight);
}

input {
  font-family: var(--font);
  font-weight: var(--font-weight);
}

.sk_theme tbody {
  color: var(--fg);
}

.sk_theme input {
  color: var(--fg);
}

/* Hints */
#sk_hints .begin {
  color: var(--accent-fg) !important;
}

#sk_tabs .sk_tab {
  background: var(--bg-dark);
  border: 1px solid var(--border);
}

#sk_tabs .sk_tab_title {
  color: var(--fg);
}

#sk_tabs .sk_tab_url {
  color: var(--main-fg);
}

#sk_tabs .sk_tab_hint {
  background: var(--bg);
  border: 1px solid var(--border);
  color: var(--accent-fg);
}

.sk_theme #sk_frame {
  background: var(--bg);
  opacity: 0.2;
  color: var(--accent-fg);
}

/* ---------- Omnibar ---------- */

.sk_theme .title {
  color: var(--accent-fg);
}

.sk_theme .url {
  color: var(--main-fg);
}

.sk_theme .annotation {
  color: var(--accent-fg);
}

.sk_theme .omnibar_highlight {
  color: var(--accent-fg);
}

.sk_theme .omnibar_timestamp {
  color: var(--info-fg);
}

.sk_theme .omnibar_visitcount {
  color: var(--accent-fg);
}

.sk_theme #sk_omnibarSearchResult ul li:nth-child(odd) {
  background: var(--bg-dark);
}

.sk_theme #sk_omnibarSearchResult ul li.focused {
  background: var(--border);
}

.sk_theme #sk_omnibarSearchArea {
  border-top-color: var(--border);
  border-bottom-color: var(--border);
}

.sk_theme #sk_omnibarSearchArea input,
.sk_theme #sk_omnibarSearchArea span {
  font-size: var(--font-size);
}

.sk_theme .separator {
  color: var(--accent-fg);
}

div.surfingkeys_match_mark {
    background-color: var(--info-fg) !important;
    color: var(--accent-fg) !important;
    opacity: 0.7;
}

/* ---------- Popup Notification Banner ---------- */
#sk_banner {
  font-family: var(--font);
  font-size: var(--banner-font-size);
  font-weight: var(--font-weight);
  background: var(--bg);
  border-color: var(--border);
  color: var(--main-fg);
  opacity: 0.9;
}

/* ---------- Popup Keys ---------- */
#sk_keystroke {
  background-color: var(--bg);
}

.sk_theme kbd .candidates {
  color: var(--info-fg);
}

.sk_theme span.annotation {
  color: var(--accent-fg);
}

/* ---------- Popup Translation Bubble ---------- */
#sk_bubble {
  background-color: var(--bg) !important;
  color: var(--fg) !important;
  border-color: var(--border) !important;
}

#sk_bubble * {
  color: var(--fg) !important;
}

#sk_bubble div.sk_arrow div:nth-of-type(1) {
  border-top-color: var(--border) !important;
  border-bottom-color: var(--border) !important;
}

#sk_bubble div.sk_arrow div:nth-of-type(2) {
  border-top-color: var(--bg) !important;
  border-bottom-color: var(--bg) !important;
}

/* ---------- Search ---------- */
#sk_status,
#sk_find {
  font-size: var(--font-size);
  border-color: var(--border);
}

.sk_theme kbd {
  background: var(--bg-dark);
  border-color: var(--border);
  box-shadow: none;
  color: var(--fg);
}

.sk_theme .feature_name span {
  color: var(--main-fg);
}


/* ---------- ACE Editor ---------- */

#sk_editor {
  background: var(--bg-dark) !important;
  height: 50% !important;
  width: 50% !important;
  color: var(--fg) !important;
  box-shadow: 0px 2px 10px var(--border-dim);
}

/* Left vertical rectangular margin, containing the line numbers */
.ace_gutter {
  background: var(--bg) !important;
  width: 14px !important;
}

/* Left line numbers alignments */
.ace_folding-enabled > .ace_gutter-cell {
  padding-left: 2px !important;
}

/* Line number and square cell */
.ace_gutter-cell {
  background: var(--bg-dim) !important;
  color: var(--main-fg) !important;
}

/* Right vertical line limit margin */
.ace_print-margin {
  background: var(--info-fg) !important;
  width: 1px !important;
  position: absolute !important;
  height: 100% !important;
}

/* Ace normal mode hidden and default cursor */
.normal-mode .ace_hidden-cursors .ace_cursor {
	background-color: transparent !important;
	border: 1px solid var(--accent-alt) !important;
	opacity: 0.7 !important;
}

/* Ace normal mode focused cursor */
.normal-mode .ace_cursor {
	border: none;
	background-color: var(--accent-alt-dim) !important;
}

/* Ace insert mode cursor */
.ace-chrome .ace_cursor {
	color: var(--main-fg) !important;
}

/* Ace text/line selection */
.ace_marker-layer .ace_selection {
  background: var(--select) !important;
}

/* Bottom command box dialog rectangle and text (:) */
.ace_dialog {
  color: var(--cyan) !important;
  background: var(--border) !important;
}
`;

/*=============
  Color Schemes
  =============*/

theme.colorSchemes = {
  tomorrowNight: `
:root {
  --font: "FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue";
  --font-weight: bold;
  --fg: #C5C8C6;
  --bg: #282A2E;
  --bg-dim: #282A2ECC;
  --bg-dark: #1D1F21;
  --border: #373B41;
  --border-dim: #373B41CC;
  --main-fg: #81A2BE;
  --accent-fg: #52C196;
  --accent-alt: #52C196;
  --accent-alt-dim: #52C19680;
  --info-fg: #AC7BBA;
  --select: #585858;
  --cyan: #4CB3BC;
  --orange: #DE935F;
  --red: #CC6666;
  --yellow: #CBCA77;
}
`,
  dracula: `
:root {
  --font: "FiraCode Nerd Font Mono", "Lilex Nerd Font Mono", "Code Neue", "Helvetica Neue";
  --font-weight: bold;
  --fg: #F8F8F2;
  --bg: #282A36;
  --bg-dim: #424450;
  --bg-dark: #21222C;
  --border: #44475A;
  --border-dim: #6272A4;
  --main-fg: #FF79C6;
  --accent-fg: #8BE9FD;
  --accent-alt: #BD93F9;
  --accent-alt-dim: #644AC980;
  --info-fg: #50FA7B;
  --select: #44475A;
  --orange: #FFB86C;
  --red: #FF5555;
  --yellow: #F1FA8C;
}
`,
  nord: `
:root {
  --font: 'Source Code Pro', Ubuntu, sans;
  --font-weight: bold;
  --fg: #E5E9F0;
  --bg: #3B4252;
  --bg-dim: #3B4252CC;
  --bg-dark: #2E3440;
  --border: #4C566A;
  --border-dim: #4C566ACC;
  --main-fg: #88C0D0;
  --accent-fg: #A3BE8C;
  --accent-alt: #8FBCBB;
  --accent-alt-dim: #8FBCBB80;
  --info-fg: #5E81AC;
  --select: #4C566A;
  --orange: #D08770;
  --red: #BF616A;
  --yellow: #EBCB8B;
}
`,
  doomOne: `
:root {
  --font: 'Source Code Pro', Ubuntu, sans;
  --font-weight: bold;
  --fg: #51AFEF;
  --bg: #2E3440;
  --bg-dim: #2E3440CC;
  --bg-dark: #21242B;
  --border: #2257A0;
  --border-dim: #2257A0CC;
  --main-fg: #51AFEF;
  --accent-fg: #98be65;
  --accent-alt: #98be65;
  --accent-alt-dim: #98be6580;
  --info-fg: #C678DD;
  --select: #4C566A;
  --border-alt: #282C34;
  --cyan: #46D9FF;
  --orange: #DA8548;
  --red: #FF6C6B;
  --yellow: #ECBE7B;
}
`,
  monokai: `
:root {
  --font: 'Source Code Pro', Ubuntu, sans;
  --font-weight: bold;
  --fg: #F8F8F2;
  --bg: #272822;
  --bg-dim: #272822CC;
  --bg-dark: #1D1E19;
  --border: #2D2E2E;
  --border-dim: #2D2E2ECC;
  --main-fg: #F92660;
  --accent-fg: #E6DB74;
  --accent-alt: #E6DB74;
  --accent-alt-dim: #E6DB7480;
  --info-fg: #A6E22E;
  --select: #556172;
  --red: #E74C3C;
  --orange: #FD971F;
  --blue: #268BD2;
  --violet: #9C91E4;
  --cyan: #66D9EF;
}
`,
  rosePine: `
:root {
  --font: "JetBrains Mono NL", "Cascadia Code", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-weight: bold;
  --fg: #E0DEF4;
  --bg: #191724;
  --bg-dim: #191724CC;
  --bg-dark: #26233A;
  --border: #524F67;
  --border-dim: #524F67CC;
  --main-fg: #C4A7E7;
  --accent-fg: #EBBCBA;
  --accent-alt: #D39C9C;
  --accent-alt-dim: #D39C9C80;
  --info-fg: #9CCFD8;
  --select: #21202E;
}
`,
  rosePineMoon: `
:root {
  --font: "JetBrains Mono NL", "Cascadia Code", "Helvetica Neue", Helvetica, Arial, sans-serif;
  --font-weight: bold;
  --fg: #E0DEF4;
  --bg: #232136;
  --bg-dim: #232136CC;
  --bg-dark: #393552;
  --border: #56526E;
  --border-dim: #56526ECC;
  --main-fg: #C4A7E7;
  --accent-fg: #EA9A97;
  --accent-alt: #D47A7A;
  --accent-alt-dim: #D47A7A80;
  --info-fg: #9CCFD8;
  --select: #2a283e;
}
`,
};


/**
 * Raw response object returned by a search completion request.
 *
 * @typedef {object} SearchEngineResponse
 * @property {string} text - Raw response text.
 */

/**
 * Extra metadata associated with a suggestion item.
 *
 * @typedef {Object.<string, unknown> & { url?: string }} SuggestionItemProps
 */

/**
 * Suggestion item returned by a completion callback.
 *
 * @typedef {object} SuggestionItem
 * @property {string} html - Rendered HTML string for the suggestion item.
 * @property {SuggestionItemProps} props - Extra metadata associated with the item.
 */

/**
 * Convert a search provider response into suggestion items.
 *
 * @callback SearchEngineCallback
 * @param {SearchEngineResponse} response - Provider response object.
 * @returns {SuggestionItem[]} Generated suggestion items.
 */

/**
 * Map of search provider callback functions.
 *
 * @typedef {Object.<string, SearchEngineCallback>} SearchEngineCallbacks
 */

/**
 * One search engine mapping entry.
 *
 * @typedef {object} SearchEngineMapping
 * @property {string} alias - Key sequence used to trigger this search engine.
 * @property {string} name - Display name of the search engine.
 * @property {string} search - Base search URL used for normal search queries.
 * @property {string} [fav_icon] - Optional icon URL shown in the omnibar.
 * @property {string} [compl] - Optional completion API URL used for suggestions.
 * @property {SearchEngineCallback} [callback] - Optional callback used to parse completion results.
 */

/**
 * Search engines registry object.
 *
 * @typedef {object} SearchEngines
 * @property {SearchEngineCallbacks} callbacks - Registered completion callbacks.
 * @property {SearchEngineMapping[]} mappings - Registered search engine mappings.
 */

/** @type {SearchEngines} */
const searchEngines = {
  callbacks: {},
  mappings: [],
};

/**
 * @typedef {object} MdnDocument
 * @property {string} title - Document title.
 * @property {string} slug - Document slug.
 * @property {string} summary - Document summary.
 * @property {string} locale - Document locale.
 */

/**
 * @typedef {object} MdnResponse
 * @property {MdnDocument[]} documents - MDN result documents.
 */

/**
 * Convert an MDN response into suggestion items.
 *
 * @type {SearchEngineCallback}
 */
searchEngines.callbacks.mdn = (response) => {
  // console.log({response})
  const res = JSON.parse(response.text);
  return res.documents.map(
    /**
     * Build one suggestion item from an MDN document.
     *
     * @param {MdnDocument} s - MDN document entry.
     * @returns {SuggestionItem}
     */
    (s) =>
      utils.createSuggestionItem(
        `
      <div>
        <div class="title"><strong>${utils.escapeHTML(s.title)}</strong></div>
        <div style="font-size:0.8em"><em>${utils.escapeHTML(s.slug)}</em></div>
        <div>${utils.escapeHTML(s.summary)}</div>
      </div>
    `,
        { url: `https://developer.mozilla.org/${s.locale}/docs/${s.slug}` }
      )
  );
};

/** @type {SearchEngineMapping[]} */
searchEngines.mappings = [
  {
    alias: "cf",
    name: "condaforge",
    search: "https://anaconda.org/search?q=",
    fav_icon: "https://localhost:9334/favicons/anaconda.ico",
  },
  {
    alias: "re",
    name: "reddit",
    search: "https://www.reddit.com/search/?q=",
    fav_icon: "https://localhost:9334/favicons/reddit.ico",
  },
  {
    alias: "go",
    name: "google",
    search: "https://google.com/search?q=",
  },
  {
    alias: "gh",
    name: "github",
    search: "https://github.com/search?q=",
  },
  {
    alias: "py",
    name: "pypi",
    search: "https://pypi.org/search?q=",
    fav_icon: "https://localhost:9334/favicons/python.ico",
  },
  {
    alias: "yt",
    name: "youtube",
    search: "https://www.youtube.com/results?search_query=",
    fav_icon: "https://localhost:9334/favicons/youtube.ico",
  },
  {
    alias: "o",
    name: "open",
    search: "https://",
    fav_icon: "https://localhost:9334/favicons/internet.ico",
  },
  {
    alias: "me",
    name: "metacritic",
    search: "https://www.metacritic.com/search/",
    fav_icon: "https://localhost:9334/favicons/metacritic.ico",
  },
  {
    alias: "fe",
    name: "firefox-extensions",
    search: "https://addons.mozilla.org/firefox/search/?q=",
    fav_icon: "https://localhost:9334/favicons/extension.ico",
  },
  {
    alias: "md",
    name: "mdn",
    search: "https://developer.mozilla.org/search?q=",
    fav_icon:
      "data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2256%22%20height%3D%2256%22%20viewBox%3D%220%200%2056%2056%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%20%20%3Ctitle%3EMDN%20Logo%3C%2Ftitle%3E%0A%20%20%3Crect%20width%3D%2256%22%20height%3D%2256%22%20fill%3D%22%2315141A%22%20%2F%3E%0A%20%20%3Cpath%20d%3D%22M22.4203%2012.5367L12.8529%2043.4192H8.91937L18.4879%2012.5322L22.4203%2012.5367Z%22%20fill%3D%22white%22%20%2F%3E%0A%20%20%3Cpath%20d%3D%22M25.9079%2012.5369V43.4193H22.4282V12.5369H25.9079Z%22%20fill%3D%22white%22%20%2F%3E%0A%20%20%3Cpath%20d%3D%22M39.4393%2012.5367L29.8719%2043.4192H25.9349L35.5024%2012.5322L39.4393%2012.5367Z%22%20fill%3D%22white%22%20%2F%3E%0A%20%20%3Cpath%20d%3D%22M42.919%2012.5369V43.4193H39.4393V12.5369H42.919Z%22%20fill%3D%22white%22%20%2F%3E%0A%3C%2Fsvg%3E%0A",
    compl: "https://developer.mozilla.org/api/v1/search?q=",
    callback: searchEngines.callbacks.mdn,
  },
];


/* Apply configuration via utils */
utils.registerShortcuts(",");

utils.loadColorScheme("rosePineMoon", "16pt", "15pt");

utils.loadVisualTheme("monokai");

utils.loadHintsTheme("tomorrowNight", "15pt", "15pt");

utils.registerSearchEngines("a", "c", "s");

/**
 * @file unmaps.js
 *
 * @description Defines specific sites and global surfingkeys keys that should be umapped.
 * Done by the `api.unmaps` function when runned `utils.loadUnmaps` function.
 *
 * Specific sites used by me that contains keymaps to execute specific actions, in case the action
 * executes a similar command from one of my custom commands, its key will necessary be unmaped to
 * be available to use, in case for other type actions, it may or may not be unmapped, based on my
 * personal need of use it.
 *
 * @see [utils](scripts/utils.js)
 */

const unmaps = {};

/*======
Unmaps
======*/

unmaps.mappings = [
  {
    keys: ["S", "ab", "af", "f", "x", "r", "<Ctrl-Alt-r>", "d", "u"],
    site: "global",
  },
  /*--------------
  Youtube Videos
  --------------*/
  {
    keys: [
      "f", // Fulscreen
      "m", // Mute/unmute
    ],
    site: "youtube.com",
  },
  {
    keys: [
      // NAVIGATION
      "?", // Show shortcuts (Shift + ?)
      "j", // Next post or comment
      "k", // Previous post or comment
      "x", // Expand/collapse content
      "l", // Copy post or comment link
      // ACTIONS
      "a", // Upvote
      "z", // Downvote
      "r", // Reply to comment
      "s", // Save/unsave
      "h", // Hide post
      "q", // Open/close navigation
      "f", // Collapse/expand comment
      "c", // Create post
      // MEDIA
      "f", // Toggle fullscreen mode
      "o", // Restart
      "m", // Mute/unmute
    ],
    site: "reddit.com",
  },
  {
    keys: [
      "j", // Next post
      "k", // Prev post
      "l", // Like/React post
      "r", // Answer
    ],
    site: "web.facebook.com",
  },
];

utils.loadUnmaps();

})();


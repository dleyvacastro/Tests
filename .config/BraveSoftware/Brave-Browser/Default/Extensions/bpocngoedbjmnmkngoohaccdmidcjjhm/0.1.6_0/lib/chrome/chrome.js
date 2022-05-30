var app = {}, mainWindow = '', whatsappWindow = '';

app.version = function () {return chrome.runtime.getManifest().version};

app.tab = {
  "open": function (url) {
    if (mainWindow) chrome.windows.update(mainWindow, {"focused": true});
    window.setTimeout(function () {chrome.tabs.create({"url": url, "active": true})}, 300);
  }
};

app.storage = (function () {
  window.setTimeout(function () {
    chrome.storage.local.get(null, function (o) {
      app.storage.GLOBAL = o;
      var script = document.createElement("script");
      script.src = "../common.js";
      document.body.appendChild(script);
    });
  }, 300);
  /*  */
  return {
    "GLOBAL": {},
    "read": function (id) {return app.storage.GLOBAL[id]},
    "write": function (id, data, callback) {
      var _tmp = {};
      _tmp[id] = data;
      app.storage.GLOBAL[id] = data;
      chrome.storage.local.set(_tmp, callback);
    }
  }
})();

chrome.windows.onFocusChanged.addListener(function (e) {
  window.setTimeout(function () {
    if (whatsappWindow && e !== whatsappWindow) {
      if (config.UI.alwaysOnTop) {
        try {chrome.windows.update(whatsappWindow, {"focused": true})} catch (e) {}
      }
    }
  }, 300);
});

app.UI = (function () {
  var r = {};
  chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
    if (request.path === 'ui-to-background') {
      for (var id in r) {
        if (r[id] && (typeof r[id] === "function")) {
          if (request.method === id) r[id](request.data);
        }
      }
    }
  });
  /*  */
  return {
    "close": function () {chrome.windows.remove(whatsappWindow)},
    "receive": function (id, callback) {r[id] = callback},
    "send": function (id, data) {
      chrome.tabs.query({}, function (tabs) {
        tabs.forEach(function (tab) {
          chrome.tabs.sendMessage(tab.id, {"path": 'background-to-ui', "method": id, "data": data}, function () {});
        });
      });
    },
    "create": function () {
      chrome.windows.getCurrent(function (win) {
        mainWindow = win.id;
        var width = config.UI.size.width;
        var height = config.UI.size.height;
        var url = "https://web.whatsapp.com/";
        var top = win.top + Math.round((win.height - height) / 2);
        var left = win.left + Math.round((win.width - width) / 2);
        chrome.windows.create({'url': url, 'type': 'popup', 'width': width, 'height': height, 'top': top, 'left': left}, function (w) {
          whatsappWindow = w.id;
        });
      });
    }
  }
})();

app.deviceReady = function (callback) {callback(true)};
app.UI.receive("deviceready", function () {app.UI.send("deviceready")});
chrome.windows.onRemoved.addListener(function (e) {if (e === whatsappWindow) {whatsappWindow = null}});
if (chrome.runtime.setUninstallURL) chrome.runtime.setUninstallURL(config.welcome.url + "?v=" + app.version() + "&type=uninstall", function () {});
chrome.browserAction.onClicked.addListener(function () {whatsappWindow ? chrome.windows.update(whatsappWindow, {"focused": true}) : app.UI.create()});

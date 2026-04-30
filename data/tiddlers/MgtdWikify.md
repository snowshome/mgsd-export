---
title: MgtdWikify
tags: systemConfig excludeSearch
created: 201106271103
modified: 201111130929
---

merge(config.macros, {
  eval: {
    handler: function(place,macroName,params,wikifier,paramString,tiddler) {
      wikify(eval(paramString),place,null,tiddler);
    }
  }
});


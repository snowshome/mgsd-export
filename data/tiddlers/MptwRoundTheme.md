---
title: MptwRoundTheme
tags: systemTheme excludeSearch
created: 201004041418
modified: 201111130925
---

|Name|MptwRounded|
|Description|Mptw Theme with some rounded corners (Firefox only)|
|ViewTemplate|MptwTheme##ViewTemplate|
|EditTemplate|MptwTheme##EditTemplate|
|PageTemplate|MptwTheme##PageTemplate|
|StyleSheet|##StyleSheet|

!StyleSheet
/*{{{*/

[[MptwTheme##StyleSheet]]

.tiddler,
.sliderPanel,
.button,
.tiddlyLink,
.tabContents
{ -moz-border-radius: 1em; }

.tab {
	-moz-border-radius-topleft: 0.5em;
	-moz-border-radius-topright: 0.5em;
}
#topMenu {
	-moz-border-radius-bottomleft: 2em;
	-moz-border-radius-bottomright: 2em;
}

/*}}}*/



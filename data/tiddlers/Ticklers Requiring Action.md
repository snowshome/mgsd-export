---
title: Ticklers Requiring Action
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

<<mgtdList
	title:'Ticklers Requiring Action'
	startTag:Tickler
	tags:'!Actioned'
	view:Tickler
	mode:global
	newButtonTags:'Tickler Enabled Once'
	where:'tiddler.ticklerIsActive()'
	sort:'tickleDate'
	dontShowEmpty:yes
	ignoreRealm:{{config.mGTD.getOptChk('AlertsIgnoreRealm')?'yes':''}}
>>


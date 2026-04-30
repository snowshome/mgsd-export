---
title: Next and Waiting Actions by Context Single Col
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

<<mgtdList startTag:Action title:'Next' tags:'Next && !Done' view:ActionProj mode:global
	group:Context
	gView:Context
	newButtonTags:'Action Next'
	where:tiddler.hasActiveProject()
	>>

<<mgtdList startTag:Action title:'Waiting' tags:'[(Waiting For)] && !Done' view:ActionProj mode:global
	group:Context
	gView:Context
	newButtonTags:'Action [(Waiting For)]'
	where:tiddler.hasActiveProject()
	>>


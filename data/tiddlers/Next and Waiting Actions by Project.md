---
title: Next and Waiting Actions by Project
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

{{cols2{

{{col{

<<mgtdList startTag:Action title:'Next' tags:'Next && !Done' view:Action mode:global
	group:Project
	gView:bold
	newButtonTags:'Action Next'
	where:tiddler.hasActiveProject()
	>>

}}}

{{col{

<<mgtdList startTag:Action title:'Waiting' tags:'[(Waiting For)] && !Done' view:Action mode:global
	group:Project
	gView:bold
	where:tiddler.hasActiveProject()
	newButtonTags:'Action [(Waiting For)]'
	>>

}}}

}}}


---
title: Next and Waiting Actions by Contact
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

{{cols2{

{{col{

<<mgtdList startTag:Action title:'Next' tags:'Next && !Done' view:ActionProj mode:global
	group:Contact
	gView:bold
	newButtonTags:'Action Next'
	where:tiddler.hasActiveProject()
	>>

}}}

{{col{

<<mgtdList startTag:Action title:'Waiting' tags:'[(Waiting For)] && !Done' view:ActionProj mode:global
	group:Contact
	gView:bold
	newButtonTags:'Action [(Waiting For)]'
	where:tiddler.hasActiveProject()
	>>


}}}

}}}


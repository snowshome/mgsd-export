---
title: SomedayMaybe and Future
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

{{cols2{

{{col{

<<mgtdList title:'Someday/Maybe Projects' startTag:Project tags:'Someday/Maybe && !Complete' view:ProjectArea mode:global
	newButtonTags:'Project Someday/Maybe'
	>>

}}}

{{col{

<<mgtdList title:'Future Actions not in Projects' startTag:Action tags:'Future && !Done' view:Action mode:global
	group:Context
	gView:Context
	newButtonTags:'Action Future'
	where:!tiddler.hasParent('Project')
	>>


}}}

}}}


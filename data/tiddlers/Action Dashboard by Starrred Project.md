---
title: Action Dashboard by Starrred Project
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

{{cols2{

{{col{

<<tiddler 'Ticklers Requiring Action'>>

<<mgtdList title:'Next Actions' startTag:Action tags:'Next && !Done' view:Action mode:global
	group:Project
	gView:bold
	where:tiddler.hasActiveProject() && tiddler.hasStarredProject
	newButtonTags:'Action Next'
	>>

}}}

{{col{


{{scroll10{

<<mgtdList title:'Done Actions' startTag:Action tags:'Done' view:DoneAction mode:global
	group:Project
	gView:bold
	sort:-modified
	newButtonTags:'Action Next Done'
	where:tiddler.hasActiveProject()
	>>

}}}

}}}

}}}


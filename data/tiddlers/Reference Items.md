---
title: Reference Items
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

{{cols2{

{{col{

<<mgtdList title:'Reference Items For Active Projects' tag:Reference startTag:Reference view:plain mode:global
	group:Project
	gView:bold
	newButtonTags:'Reference'
	where:tiddler.hasActiveProject()
	>>

}}}

{{col{

<<mgtdList title:'Other Reference Items' tag:Reference startTag:Reference view:plain mode:global
	group:Project
	gView:bold
	newButtonTags:'Reference'
	where:!tiddler.hasActiveProject()
	>>

}}}

}}}


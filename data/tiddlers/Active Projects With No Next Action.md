---
title: Active Projects With No Next Action
tags: View excludeSearch
created: 201003270648
modified: 201111130929
---

(shows active projects without a next action, sub-project or upcoming tickler)

<<mgtdList startTag:Project title:'You must assign a next action to these projects (or make them into Someday/Maybe)'
	tags:'!Complete && !Someday/Maybe' view:Project mode:global
	where:!tiddler.hasNextActionOrSubProjectOrTickler()
	>>


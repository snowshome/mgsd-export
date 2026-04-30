---
title: StarredProjectsAndTasks
tags: 
created: 202505262312
modified: 202505262313
---

! Starred Projects and Tasks

<$list filter="[tag[project]tag[starred]]">
!! {{!!title}}
<$list filter="[tag[task]project<currentTiddler>]">
- {{!!title}}
</$list>
</$list>

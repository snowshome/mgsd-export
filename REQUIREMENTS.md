# mGSD Requirements (from Classic TiddlyWiki)

## Core Entity Types (via tags)
- **Project**: `Project` + `Active` / `Inactive` / `Someday`
- **Action/Task**: `Action` + `Next` / `Waiting` / `Done`
- **Contexts**: `Home`, `Work`, `Errands`, `Computer`, `Phone`, etc.
- **Areas**: `Personal`, `Family`, `Work`, etc.
- **Views**: `View` tag (Starred Items, etc.)

## Key Relationships
- Actions link to Projects via wikilinks in tags or text (e.g. `[[test Project3]]`)
- Priorities / Status via additional tags (`Active`, `Next`, `Waiting`)

## Current Views / Navigation (to replicate)
- Starred Items view
- Next Actions list
- Active Projects dashboard
- Waiting For list
- Context-based lists (Home, Errands, etc.)
- Clickable navigation between Projects ↔ Actions
- Weekly/Monthly review support

## Special Behaviors
- Automatic "Next Action" detection per project
- Tag-driven filtering and dynamic lists
- Exclude system tiddlers from normal searches

## Goal
Replicate all of the above in Obsidian with zero data lock-in, using markdown files + plugins.
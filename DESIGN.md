# Obsidian mGSD Design

## Folder Structure (PARA + GTD)
- `10 Projects/`
- `20 Areas/`
- `30 Resources/`
- `40 Archive/`
- `00 Inbox.md`
- `Dashboard.md`

## Plugin Stack
- **Dataview** → dynamic queries replacing mGSD views
- **Tasks** → replaces Action tracking (due dates, priorities, repeats)
- **Templater** / QuickAdd → fast capture
- **Kanban** (optional) → visual project boards

## Tag Mapping → Obsidian

| mGSD Tag          | Obsidian Equivalent                  |
|-------------------|--------------------------------------|
| `Project`         | Folder `10 Projects/` + `#project`   |
| `Action`          | `- [ ]` Tasks + `#action`            |
| `Next`            | `#next` or Tasks status              |
| `Waiting`         | `#waiting`                           |
| `Active`          | `#active`                            |
| `Home` / `Errands`| `#context/home`                      |
| `Personal`        | `#area/personal`                     |

## Core Queries (for Dashboard.md)

**Next Actions**
```dataview
TASK
WHERE contains(tags, "Next") OR status = " "
AND !completed
SORT priority DESC

## Desired Views (Priority)

### 1. All Projects View
- List of all tiddlers tagged `Project`
- Show status (`Active` / `Inactive`)
- Count of Next Actions per project

### 2. Single Project View
- Inside each Project note: embedded list of its Actions (Next / Waiting)
- Quick links to related Areas

### 3. Tag Overview
- All tags with counts + clickable list of items using that tag

## Implementation in Obsidian

### 1. All Projects (create `Dashboard.md`)
```dataview
TABLE file.mtime as "Last Updated", length(rows) as "Next Actions"
FROM "10 Projects"
WHERE contains(tags, "Project")
FLATTEN file.tasks as tasks
GROUP BY file.link
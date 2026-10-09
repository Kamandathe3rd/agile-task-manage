# Agile Task Manager — Sprint Plan

## Product Vision
Build a simple task manager that helps users create, view, complete, and delete tasks. Use automated tests and CI to maintain software quality.

## Product Backlog

| ID | User Story | Priority | Points |
|---|---|---|---:|
| US1 | As a user, I want to add tasks. | High | 2 |
| US2 | As a user, I want to view all tasks. | High | 2 |
| US3 | As a user, I want to mark tasks complete. | High | 3 |
| US4 | As a user, I want to delete tasks. | Medium | 2 |
| US5 | As a maintainer, I want automated tests in CI. | High | 3 |
| US6 | As a maintainer, I want logs and a health endpoint. | Medium | 2 |

## Acceptance Criteria

- US1: A valid task is saved; an empty task is rejected.
- US2: The task list is returned successfully.
- US3: Completing a task changes its status to true.
- US4: Deleting a task removes it from the list.
- US5: Tests run automatically when code is pushed to GitHub.
- US6: `/health` returns a healthy status and important actions are logged.

## Definition of Done (DoD)

- Code is written and committed to Git.
- Acceptance criteria are met.
- Automated tests pass.
- Changes are reviewed.
- CI checks pass.
- Documentation is updated.

## Sprint 1 Plan

Duration: Simulated 1 week.

Selected stories: US1, US2, US5.

Goal: Deliver task creation and listing with automated tests and CI.

## Sprint 2 Plan

Duration: Simulated 1 week.

Selected stories: US3, US4, US6.

Goal: Add task completion, deletion, logging, and a health endpoint.
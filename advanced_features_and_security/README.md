# Task 1: Managing Permissions and Groups

## Custom Permissions
The Book model defines the following custom permissions:
- can_view
- can_create
- can_edit
- can_delete

## Groups
The following groups were created using the Django admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

## Permission Enforcement
Permissions are enforced in views using the @permission_required decorator.
Users without the required permissions receive a 403 Forbidden response.

## Testing
Test users were created and assigned to groups to ver
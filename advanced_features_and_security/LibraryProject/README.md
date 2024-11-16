# Django Custom Permissions & User Management

This project demonstrates how to implement custom user models, permissions, and enforce them on views in a Django application. The goal is to create a user management system where different user groups can have specific permissions for actions like creating, editing, and deleting instances of models.

## Features

1. **Custom User Model**: A custom user model where email is the unique identifier for authentication, and additional fields can be added.
2. **Custom Permissions**: Create custom permissions such as `can_view`, `can_create`, `can_edit`, and `can_delete` to control user access to specific model actions.
3. **Groups & Permissions**: Users are grouped into roles (like `Admins`, `Editors`, and `Viewers`), and specific permissions are assigned to these groups.
4. **Permissions Enforcement in Views**: Permissions are enforced using the `@permission_required` decorator to protect views from unauthorized users.
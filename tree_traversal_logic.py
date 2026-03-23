import random
import time
from collections import deque
from tree_node import TreeNode

# Colors (since settings edit failed)
COLOR_TREE_NODE = "#4cc9f0"
COLOR_TREE_VISIT = "#f72585"
COLOR_TREE_PRE = "#00b4d8"
COLOR_TREE_IN = "#90be6d"
COLOR_TREE_POST = "#f8961e"
COLOR_TREE_LEVEL = "#f5a623"
ANIMATION_DELAY = 0.03  # Reuse from settings

def generate_random_tree(max_depth=5, max_val=99):
    """Generate random binary tree for demo."""
    if random.random() < 0.1 or max_depth == 0:
        return None
    node = TreeNode(random.randint(1, max_val))
    node.left = generate_random_tree(max_depth - 1, max_val)
    node.right = generate_random_tree(max_depth - 1, max_val)
    return node

def run_traversal(app, traversal_type):
    if not app.root_node:
        app.status_var.set("No tree! Click 'Random Tree' first.")
        return
    app.running = True
    app.btn_clear.config(state="disabled")
    app.status_var.set(f"Running {traversal_type} traversal...")
    app.root.update()

    visit_order = get_traversal(app.root_node, traversal_type)
    
    colors = {
        'preorder': COLOR_TREE_PRE,
        'inorder': COLOR_TREE_IN,
        'postorder': COLOR_TREE_POST,
        'levelorder': COLOR_TREE_LEVEL
    }
    color = colors.get(traversal_type, COLOR_TREE_VISIT)

    for node in visit_order:
        app.highlight_node(node, color)
        app.root.update()
        time.sleep(ANIMATION_DELAY)

    app.status_var.set(f"{traversal_type.title()} complete: {len(visit_order)} nodes visited.")
    app.running = False
    app.btn_clear.config(state="normal")

def get_traversal(root, traversal_type):
    """Return visit order for traversal type."""
    if traversal_type == 'preorder':
        return preorder(root)
    elif traversal_type == 'inorder':
        return inorder(root)
    elif traversal_type == 'postorder':
        return postorder(root)
    elif traversal_type == 'levelorder':
        return levelorder(root)
    return []

def preorder(root):
    result = []
    def dfs(node):
        if node:
            result.append(node)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

def inorder(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node)
            dfs(node.right)
    dfs(root)
    return result

def postorder(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node)
    dfs(root)
    return result

def levelorder(root):
    result = []
    if not root:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


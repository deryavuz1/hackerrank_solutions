def lca(root, v1, v2):

    if v1 >= root.info and v2 <= root.info or v2 >= root.info and v1 <= root.info:
        return root
    
    if v1 > root.info and v2 > root.info:
        return lca(root.right, v1, v2)
    elif v1 < root.info and v2 < root.info:
        return lca(root.left, v1, v2)
    

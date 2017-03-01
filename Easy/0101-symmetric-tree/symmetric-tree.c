struct Node
{
    int key;
    struct Node* left, *right;
};

struct Node *newNode(int key)
{
    struct Node *temp;
    temp->key  = key;
    temp->left  = temp->right = NULL;
    return (temp);
}

bool isMirror(struct Node *root1, struct Node *root2)
{
    if (root1 == NULL && root2 == NULL)
        return true;
    if (root1 && root2 && root1->key == root2->key)
        return isMirror(root1->left, root2->right) &&
               isMirror(root1->right, root2->left);
    return false;
}

bool isSymmetric(struct Node* root)
{
    return isMirror(root, root);
}
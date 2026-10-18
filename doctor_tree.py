
# Hospital Doctor Reporting Tree

class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    # Add a doctor under an existing manager
    def insert(self, parent_name, doctor_name, side):
        side = side.strip().lower()

        if side not in ("left", "right"):
            print("Invalid side. Choose left or right.")
            return False

        if self.root is None:
            print("Add a root doctor first.")
            return False

        return self._insert_recursive(
            self.root, parent_name, doctor_name, side
        )

    # Recursively search for the correct manager
    def _insert_recursive(self, node, parent_name, doctor_name, side):
        if node is None:
            return False

        if node.name == parent_name:
            if getattr(node, side) is not None:
                print("That reporting position is already occupied.")
                return False

            setattr(node, side, DoctorNode(doctor_name))
            return True

        if self._insert_recursive(node.left, parent_name, doctor_name, side):
            return True

        return self._insert_recursive(
            node.right, parent_name, doctor_name, side
        )

    # Root, left, right
    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    # Left, root, right
    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    # Left, right, root
    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


# Test the doctor reporting tree
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Check invalid insertions
    print("\nTesting errors:")
    tree.insert("Dr. Missing", "Dr. Test", "left")
    tree.insert("Dr. Croft", "Dr. Test", "middle")
    tree.insert("Dr. Croft", "Dr. Test", "left")

    print("\nDoctor tree testing complete.")

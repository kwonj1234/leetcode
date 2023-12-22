class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        new_path = []

        for filename in path:
            if filename == ".":
                continue
            elif filename == "..":
                if new_path:
                    new_path.pop()
            elif filename:
                new_path.append(filename)

        if new_path:
            return "/" + "/".join(new_path)
        return "/"
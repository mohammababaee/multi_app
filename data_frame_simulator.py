class MyDataFrame:
    def __init__(self, data=None, columns=None):
        self.data = data or []
        self.columns = columns or []

    def load_data(self, data, columns=None):
        self.data = data
        self.columns = columns or [f"Column_{i+1}" for i in range(len(data[0]))]

    def describe(self):
        description = {
            col: {
                "count": len(self.data),
                "unique": len(set(row[i] for row in self.data)),
            }
            for i, col in enumerate(self.columns)
        }
        return description

    def head(self, n=5):
        return [self.columns] + self.data[:n]

    def index(self, row_index):
        if not 0 <= row_index < len(self.data):
            raise IndexError("Index out of range")
        return self.data[row_index]

    def sort(self, column, mode="ascending"):
        if column not in self.columns:
            raise ValueError(f"Column '{column}' not found")

        col_index = self.columns.index(column)
        sorted_data = sorted(
            self.data,
            key=lambda x: x[col_index],
            reverse=(mode.lower() == "descending"),
        )
        return MyDataFrame(sorted_data, self.columns)

    def __repr__(self):
        rows = [self.columns] + self.data
        max_lens = [
            max(len(str(row[i])) for row in rows) for i in range(len(self.columns))
        ]
        formatted_rows = [
            "  ".join(str(cell).ljust(max_len) for cell, max_len in zip(row, max_lens))
            for row in rows
        ]
        return "\n".join(formatted_rows)

    def __getattr__(self, column):
        if column in self.columns:
            col_index = self.columns.index(column)
            return [row[col_index] for row in self.data]
        raise AttributeError(f"'MyDataFrame' object has no attribute '{column}'")

    def __getitem__(self, columns):
        if isinstance(columns, str):
            if columns not in self.columns:
                raise KeyError(f"Column '{columns}' not found")
            return [row[self.columns.index(columns)] for row in self.data]
        elif isinstance(columns, list):
            if not all(col in self.columns for col in columns):
                raise KeyError(f"One or more columns not found")
            selected_data = [
                [row[self.columns.index(col)] for col in columns] for row in self.data
            ]
            return MyDataFrame(selected_data, columns)
        raise TypeError("Invalid column selection")


# Example usage
data = [(1, 2, 3), (4, None, 10), (5, 1, 19)]
columns = ["a", "b", "c"]

my_df = MyDataFrame(data, columns)
print(my_df)
print(my_df.a)
print(my_df.index(1))
print(
    my_df[
        [
            "a",
            "c",
        ]
    ]
)
sorted_df = my_df.sort("a", mode="ascending")
print(sorted_df)

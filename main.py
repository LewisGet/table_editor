class table_editor():
    #put your content in here.
    Content = """1	2	3	4
	5	6	7
8	9	0	1
8	9	0	1"""

    Rows = []

    def content_decode(self):
        for row in self.Content.split("\n"):
            columns = []
            for column_content in row.split("\t"):
                columns.append(column_content)

            self.Rows.append(columns)

    def pre_row_html(self, row_index, column_index):
        #put your style in here.
        if column_index == 0:
            return "background: #cccccc";

        if row_index % 2 == 1:
            return "background:#000000; color: #ffffff"

        return ""

    def row_html(self, row, row_index):
        html = "    <tr>\n"

        for column_index, column in enumerate(row):
            style = self.pre_row_html(row_index, column_index)

            if style is not "":
                html += self.column_html(column, style)
            else:
                html += self.column_html(column)

        return html + "    </tr>\n"

    def column_html(self, content, style=""):
        if style is not "":
            return "        <td style=\"" + style + "\">" + content + "</td>\n"

        return "        <td>" + content + "</td>\n"

    def table_html(self, rows):
        html = "<table>\n"

        for row_index, row in enumerate(rows):
            html += self.row_html(row, row_index)

        return html + "</table>\n"

    def __init__(self):
        self.content_decode()

table = table_editor()
print (table.table_html(table.Rows))

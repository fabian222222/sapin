from flask import Flask, render_template

app = Flask(__name__)
@app.route('/sapin/<size>')
def tree(size):
    size = int(size)
    if size <= 0 or size > 30:
        return "The size of your tree must be between 0 and 30"
    tree_size = 4
    line_size = 1
    tree_result = []
    trunk_result = ["|"]
    trunk_thickness = 1
    for block in range(1, size + 1):
        if block % 2 == 0 :
            trunk_result.append('|')
            trunk_result.append('|')
            trunk_thickness += 2
        tree_temporary = []
        for branch in range(1, tree_size +  1):
            branch_temporary = []
            for star in range(1, line_size + 1):
                branch_temporary.append("*")
            line_size += 2
            tree_temporary.append(branch_temporary)
        tree_result.append(tree_temporary)
        if tree_size%2 == 0:
            line_size = len(tree_temporary[int(tree_size/2)])
        else :  
            line_size = len(tree_temporary[round((tree_size + 1) / 2)])
        tree_size += 1
    return render_template('index.html', results=tree_result, trunks=trunk_result, trunk_width=size)
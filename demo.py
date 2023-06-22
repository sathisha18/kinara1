from flask import Flask, request, jsonify
import csv
import json

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    file_path = 'students.csv'  # Replace with your actual file path

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        students = list(reader)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    paginated_students = students[start_index:end_index]

    return jsonify(paginated_students)

@app.route('/students/filter', methods=['GET'])
def filter_students():
    filter_criteria = request.args.get('filter_criteria')
    file_path = 'students.csv'  # Replace with your actual file path

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        students = list(reader)

    filtered_students = []

    # Implement your filtering logic here based on the filter criteria
    # Add the filtered students to the 'filtered_students' list

    return jsonify(filtered_students)

if __name__ == '__main__':
    app.run(debug=True)

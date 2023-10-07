from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
  {"id": 1, "title": "Complete project proposal", "description": "Write and submit the project proposal by Friday.", "due_date": "2023-10-12", "priority": "High"},
  {"id": 2, "title": "Create design mockups", "description": "Create design mockups.", "due_date": "2023-10-20", "priority": "Medium"},
  {"id": 2, "title": "Review design mockups", "description": "Review and provide feedback on design mockups.", "due_date": "2023-10-23", "priority": "High"},
  {"id": 2, "title": "Start coding for the mockups", "description": "Start coding for the mockup designs.", "due_date": "2023-11-15", "priority": "High"}
]

# Create a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
  new_task = request.get_json()
  new_task["id"] = len(tasks) + 1
  tasks.append(new_task)
  return jsonify(new_task), 201

# Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
  return jsonify(tasks)

# Get a specific task by ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = next((task for task in tasks if task["id"] == task_id), None)
  if task is None:
    return jsonify({"message": "Task not found"}), 404
  return jsonify(task)

# Update a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  task = next((task for task in tasks if task["id"] == task_id), None)
  if task is None:
    return jsonify({"message": "Task not found"}), 404
  updated_task_data = request.get_json()
  task.update(updated_task_data)
  return jsonify(task)

# Delete a task by ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  task = next((task for task in tasks if task["id"] == task_id), None)
  if task is None:
    return jsonify({"message": "Task not found"}), 404
  tasks.remove(task)
  return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
  app.run(debug=True)

//https://snack.expo.io/@nancyruya/5567fd

import React from 'react';
import { render } from 'react-dom';

let id = 0

const Task = props => (
  <li>
    <input type="checkbox" checked={props.task.checked} onChange={props.onToggle} />
    <button onClick={props.onDelete}>delete</button>
    <span>{props.task.text}</span>
  </li>
)

class App extends React.Component {
  constructor() {
    super()
    this.state = {
      tasks: [],
    }
  }

  addTask() {
    const text = prompt("Add task please!")
    this.setState({
      tasks: [
        ...this.state.tasks,
        {id: id++, text: text, checked: false},
      ], 
    })
  }

  removeTask(id) {
    this.setState({
      tasks: this.state.tasks.filter(task => task.id !== id)
    })
  }

  toggleTask(id) {
    this.setState({
      tasks: this.state.tasks.map(task => {
        if (task.id !== id) return task
        return {
          id: task.id,
          text: task.text,
          checked: !task.checked,
        }
      })
    })
  }

  render() {
    return (
      <div>
        <div>Task count: {this.state.tasks.length}</div>
        <div>Unchecked task count: {this.state.tasks.filter(task => !task.checked).length}</div>
        <button onClick={() => this.addTask()}>Add TASK</button>
        <ul>
          {this.state.tasks.map(task => (
            <Task
              onToggle={() => this.toggleTask(task.id)}
              onDelete={() => this.removeTask(task.id)}
              task={task}
            />
          ))}
        </ul>
      </div>
    )
  }
}


render(<App />, document.getElementById('root'));

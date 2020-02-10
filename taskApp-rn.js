import React from 'react';
import {View, Button, Text, ScrollView, StyleSheet, Switch} from 'react-native'
import Constants from 'expo-constants'


let id = 0

const styles = StyleSheet.create({
  taskContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  appContainer: {
    paddingTop: Constants.statusBarHeight,
  },
  fill: {
    flex: 1,
  }
})

const Task = props => (
  <View style={styles.taskContainer}>
    <Switch value={props.task.checked} onValueChange={props.onToggle} />
    <Button onPress={props.onDelete} title="delete" />
    <Text>{props.task.text}</Text>
  </View>
)

export default class App extends React.Component {
  constructor() {
    super()
    this.state = {
      tasks: [],
    }
  }

  addTask() {
    id++
    const text = `TASK number ${id}`
    this.setState({
      tasks: [
        ...this.state.tasks,
        {id: id, text: text, checked: false},
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
      <View style={[styles.appContainer, styles.fill]}>
        <Text>Task count: {this.state.tasks.length}</Text>
        <Text>Unchecked task count: {this.state.tasks.filter(task => !task.checked).length}</Text>
        <Button onPress={() => this.addTask()} title="Add TASK" />
        <ScrollView style={styles.fill}>
          {this.state.tasks.map(task => (
            <Task
              onToggle={() => this.toggleTask(task.id)}
              onDelete={() => this.removeTask(task.id)}
              task={task}
            />
          ))}
        </ScrollView>
      </View>
    )
  }
}

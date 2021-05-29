import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import Course from './src/components/Course';
import { Provider as ReduxProvider } from "react-redux";
import store from "./src/redux/store";
import Search from './src/components/Search.pages';

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import CreateCourseScreen from './src/components/screens/CreateCourse.screen';
import MyCourses from './src/components/screens/MyCourses.screen';




const Stack = createStackNavigator();

export default function App() {
  return (
    <ReduxProvider store={store}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={CreateCourseScreen} />
          <Stack.Screen name="MyCourses" component={MyCourses} />
          <Stack.Screen name="Search" component={Search} />
        </Stack.Navigator>
      </NavigationContainer>
    </ReduxProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

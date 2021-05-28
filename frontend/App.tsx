import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Course from './src/components/Course';
import { Provider as ReduxProvider } from "react-redux";
import store from "./src/redux/store";

export default function App() {
  return (
    <ReduxProvider store={store}>
      <View style={styles.container}>
        <Course />
        <StatusBar style="auto" />
      </View>
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

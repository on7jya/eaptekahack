import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';
import Course from '../Course';
const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
});

export default function CreateCourseScreen({ navigation }: any) {
    return (

        <View style={styles.container}>
            <Button
                title="Go to Details"
                onPress={() => navigation.navigate('MyCourses')}
            />
            <Course />
        </View>

    );
}
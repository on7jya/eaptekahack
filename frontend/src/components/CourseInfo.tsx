import React from 'react'
import { LinearProgress } from 'react-native-elements';
import { StyleSheet, Text, View } from 'react-native';
export default function CourseInfo(props: any) {
    const { course } = props;
    console.log(props)
    return (
        <View>
            <Text>{course.title}</Text>
            <Text>{course.count + ' препарата'}</Text>
            <LinearProgress color="primary" value={course.progress} />
            <Text>{course.progress + '%'}</Text>
        </View>

    )
}

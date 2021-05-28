import React from 'react'
import { Text, View } from 'react-native'
import { useSelector } from 'react-redux'
import { RootState } from '../redux/store'
import { MainState } from '../types/redux.types';

export default function Course() {
    const course: MainState = useSelector<RootState>(state => state.main);
    return (
        <View>
            <Text>{course.drug}</Text>
            <Text>{course.quantity}</Text>
            <Text>Таблетки</Text>
        </View>
    )
}

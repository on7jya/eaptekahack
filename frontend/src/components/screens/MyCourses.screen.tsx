import React from 'react';
import { StyleSheet, Text, View, Button } from 'react-native';

export default function MyCourses({ navigation }: any) {
    return (
        <View>
            <Text>Your courses</Text>
            <Button
                title="Go to Details"
                onPress={() => navigation.navigate('Home')}
            />
        </View>
    )
}
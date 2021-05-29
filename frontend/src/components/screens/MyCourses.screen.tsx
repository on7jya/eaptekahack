import React from 'react';
import { StyleSheet, Text, View, Button, FlatList } from 'react-native';
import Icon from 'react-native-vector-icons/FontAwesome';
import CourseInfo from '../CourseInfo';
import EncourageAlert from '../EncourageAlert';

export default function MyCourses({ navigation }: any) {
    const handleAdd = () => {

    }
    const renderItem = ({ item }: any) => (
        < CourseInfo course={item} />
    )

    return (
        <View style={styles.container}>
            <Text>Мои курсы</Text>
            <EncourageAlert />
            <Icon
                onPress={() => { handleAdd() }}
                name='plus'
                size={24}
                color='black'
            />
            <Text>Активные курсы</Text>
            <FlatList
                data={[{ title: 'hello', progress: 75, count: 2 }]}
                renderItem={renderItem}
            // keyExtractor={item => item.id}
            />
            <Text>Архивные курсы</Text>
            <Button
                title="Go to Details"
                onPress={() => navigation.navigate('Home')}
            />
        </View >
    )
}
const styles = StyleSheet.create({
    container: {
        display: 'flex',
        alignItems: 'center',

    }
})
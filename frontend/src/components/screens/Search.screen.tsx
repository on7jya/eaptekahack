import React, { useState } from 'react';
import { StyleSheet, FlatList, Text, View, Button, TextInput } from 'react-native';
import { Input } from 'react-native-elements';
import Icon from 'react-native-vector-icons/FontAwesome';
import { useAction } from '../../utils/useAction';

export default function Search({ navigation }: any) {

    const [drugName, setDrugName] = useState<string>('');
    const { requestCourses } = useAction();
    const handleRemove = () => {
        setDrugName('');
    }
    const renderItem = ({ item }: any) => (
        <View>
            <Text >{item.text}</Text>
            <Text>{item.price + 'руб.'}</Text>
        </View>
    );
    return (

        <View>
            <Input
                onChangeText={(e) => { setDrugName(e) }}
                placeholder='50 000 лекарств и товаров'
                value={drugName}
                rightIcon={
                    <Icon
                        onPress={() => { handleRemove() }}
                        name='times'
                        size={24}
                        color='black'
                    />
                } />
            <Button title='click me' onPress={() => requestCourses()} />
            <FlatList
                data={[{ text: 'hello', id: 0, price: 100 }]}
                renderItem={renderItem}
                keyExtractor={item => item.id}
            />
        </View>
    )
}
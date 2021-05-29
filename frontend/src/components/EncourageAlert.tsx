import React from 'react'
import { StyleSheet, Text, View, Image } from 'react-native';

export default function EncourageAlert() {
    return (
        <View style={styles.container}>
            {/* <Image
                style={styles.tinyLogo}
                source={require('../assets/smile1.png')}
            /> */}
            <Image
                style={styles.tinyLogo}
                source={require('../assets/close.png')}
            />
            <View>
                <Image
                    style={styles.trophyImg}
                    source={require('../assets/trophy.png')}
                />
                <Text>Отличный прогресс!</Text>
            </View>

        </View>
    )
}
const styles = StyleSheet.create({
    container: {
        position: 'relative',
        width: '343px',
        height: '159px',
        backgroundColor: '#5D66D3',
        borderRadius: 4
    },
    tinyLogo: {
        width: '24px',
        height: '24px',
        position: "absolute",
        top: '10px',
        right: '10px'
    },
    trophyImg: {
        width: '30px',
        height: '36px',
    }
})
import React from 'react';
import {
    View,
    Text,
    Dimensions,
    StyleSheet
} from 'react-native';

export default props => (
    <View style={styles.container}>
        <Text style={styles.text}>{props.snippet}</Text>
    </View>
)

const styles = StyleSheet.create({
    container: {
        margin: 5,
        backgroundColor: "#EE5C53",
        padding: 15,
        width: Dimensions.get('window').width
    },
    text: {
        fontSize: 15,
        color: "white",
    }
})
import React from 'react';
import {
    View,
    TextInput,
    Dimensions,
    StyleSheet
} from 'react-native'

export default props => (
    <View>
        <TextInput
            onChangeText={text => props.handleChange(text)}
            value={props.claim}
            style={styles.textInput}
            placeholder="Digite o Fato"
            placeholderTextColor="white"
        />
    </View>
)

const styles = StyleSheet.create({
    textInput: {
        height: 50,
        width: Dimensions.get('window').width,
        backgroundColor: "#EE5C53",
        padding: 15,
        color: "white",
        marginTop: 30,
        fontSize: 15
    },
})
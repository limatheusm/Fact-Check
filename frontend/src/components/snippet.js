import React from 'react';
import {
    View,
    Text,
    Dimensions,
    StyleSheet
} from 'react-native';
import Hyperlink from 'react-native-hyperlink'

export default props => (
    <View style={styles.container}>
        {console.log(props)}
        <Text style={styles.phrase}>"{props.snippet.phrase}"</Text>
        <Text style={styles.results}>{props.snippet.results}</Text>
        <Text style={styles.title}>{props.snippet.title}</Text>
        <Text style={styles.description}>{props.snippet.description}</Text>
        <Hyperlink linkDefault={ true }>
            <Text style={styles.link}>{props.snippet.url}</Text>
        </Hyperlink>
    </View>
)

const styles = StyleSheet.create({
    container: {
        margin: 10,
        backgroundColor: "#EE5C53",
        padding: 15,
        width: Dimensions.get('window').width - 20
    },
    phrase: {
        fontSize: 18,
        color: "white",
        fontFamily: 'Avenir',
        alignSelf: 'center',
        fontWeight: 'bold',
        textAlign: 'center',
        marginBottom: 15
    },
    results: {
        fontSize: 12,
        color: "white",
        backgroundColor: "#3b73ab",
        fontFamily: 'Chalkboard SE',
        alignSelf: 'center',
        marginBottom: 5,
        padding: 5
    },
    title: {
        fontSize: 15,
        color: "white",
        fontFamily: 'Chalkboard SE',
        fontWeight: 'bold',
        marginBottom: 5,
        marginTop: 15,
    },
    description: {
        fontSize: 12,
        color: "white",
        fontFamily: 'Chalkboard SE',
        textAlign: 'justify'
    },
    link: {
        fontSize: 15,
        color: "#0066ff",
        marginTop: 15,
        fontStyle: 'italic',
        textDecorationLine: 'underline'
    }
})
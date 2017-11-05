import React, { Component } from 'react';
import {
    Button,
    View,
    Dimensions,
    StyleSheet,
    ActivityIndicator
} from 'react-native';
import net from 'react-native-tcp';

import Claim from './claim'
import Header from './header'
import Snippet from './snippet'

export default class AnalyzerService extends Component {
    constructor(props) {
        super(props);
        this.PORT = 5050;
        this.state = { claim: '', snippets: [], loading: false };
        this.handleChangeClaim = this.handleChangeClaim.bind(this);
    };

    getSnippets() {

        // Apagar snippets anteriores
        this.setState({...this.state, snippets: []})

        // Conecta via Socket TCP ao backend
        let client = net.createConnection(this.PORT);

        // Envia msg
        client.write(this.state.claim);
        
        // Starta loading
        this.setState({ ...this.state, loading: true });

        // Retorno do server
        client.on('data', data => {
            let snippets = JSON.parse(data).phrases;
            console.log(snippets);
            this.setState({ ...this.state, snippets, loading: false });
            client.destroy(); // kill client after server's response
        });
    }

    clear() {
        this.setState({ ...this.state, claim: '', snippets: [], loading: false });
    }

    handleChangeClaim(claim) {
        this.setState({ ...this.state, claim });
    }

    renderActivityIndicator() {
        if (this.state.loading) {
            return <ActivityIndicator color='white' />;
        }
    }

    render() {
        const { container, header, textInput, btn, buttonView, claim } = styles
        return (
            <View style={container}>
                <Header />
                <Claim
                    handleChange={this.handleChangeClaim}
                    claim={this.state.claim}
                />
                <View style={buttonView}>
                    <Button
                        style={btn}
                        title='Check'
                        color='white'
                        onPress={() => this.getSnippets()}
                    />
                    <Button
                        style={btn}
                        title='Clear'
                        color='white'
                        onPress={() => this.clear()}
                    />
                </View>
                {this.state.snippets.map(snippet => <Snippet key={snippet} snippet={snippet} />)}
                {this.state.loading ? <ActivityIndicator color='white' /> : false}
            </View>
        )
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        //justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#3b73ab',
    },
    welcome: {
        fontSize: 20,
        textAlign: 'center',
        margin: 10,
    },
    buttonView: {
        flexDirection: 'row',
        margin: 20
    },
    btn: {
        marginLeft: 40
    }
});

import React from 'react'
import {
    View,
    Image,
    Dimensions,
} from 'react-native';

export default props => (
    <View>
        <Image 
            style={{width: 380, height: 200, marginTop: 25}}
            source={require('../img/debate.png')}
        />
    </View>
)
import React, { Component } from 'react';
import axios from 'axios'

class Display extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            avg: null
        };
    }

    componentDidMount() {
        debugger;
        if (this.state.avg === null) {
            const getAvg = async () => await axios.get('/api/avg/');
            const avg = getAvg();
            this.setState({avg: avg})
        }
    }

    render() {
        return (
            <div>
                <h1>Display</h1>
                <h2>{this.state.avg}</h2>
            </div>
        )
    }
}

export default Display;
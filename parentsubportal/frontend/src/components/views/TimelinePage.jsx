import React, { Component } from "react";
import { Menu, Icon, Popup, Header } from "semantic-ui-react";

class TimelinePage extends Component {
    state = { activeItem: "video" };

    handleItemClick = (e, { name }) => this.setState({ activeItem: name });

    render() {
        const { activeItem } = this.state;

        return Hi;
    }
}

export default withRouter(TimelinePage);

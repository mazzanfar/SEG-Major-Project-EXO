import React, { Component } from 'react';
import { Menu, Icon, Dropdown } from 'semantic-ui-react';

class TopMenu extends Component {

    render() {
        return (
            <Menu pointing secondary fixed="top">
                <Menu.Menu>
                    <Menu.Item>
                        Dashboard
                    </Menu.Item>
                </Menu.Menu>

            <Menu.Item name="home">
                <span>Home</span>
            </Menu.Item>
            </Menu>
        ) 
    }
}

export default TopMenu;

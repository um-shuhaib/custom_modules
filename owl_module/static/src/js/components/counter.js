/** @odoo-module **/
import {registry} from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
// const {Component,useState} = owl;

export class NewField extends Component{
    setup(){
        this.state = useState({value:0})
    }

    increment(){
        this.state.value++;
    }
    decrement(){
        if (this.state.value > 0){
            this.state.value--;
        }
    }


    }
NewField.template = 'owl_module.TodoList'

registry.category("actions").add("owl_module.todo_list",NewField)
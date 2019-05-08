class Dom {
        
    constructor(){
        this.elements = [];
        this.indexDirectory = new Map();
        this.notificationDirectory = new Map();
    }

    registerProvider(providerId){
        this.notificationDirectory.set(providerId,[]);
    }

    registerSubscriber(providerId,subscriberId){
        let subs = this.notificationDirectory.get(providerId);
        subs.push(subscriberId);
        this.notificationDirectory.set(providerId, subs);
    }

    registerElement(element){
        if(this.indexDirectory.has(element.id))
            console.log(`El elemento con id: ${element.id} ya está registrado`);
        else {
            this.elements.push(element);
            this.indexDirectory.set(element.id,this.elements.length-1);
        }
    }

    show(){
        console.log("IndexDirectory",this.indexDirectory);
        console.log("Elements",this.elements);
        console.log("NotificationDirectory", this.notificationDirectory);
    }

    static newElement(tagName, classname=null, id=null, innerText=null){
        
        let element = document.createElement(tagName);

        if(classname != null)
            element.setAttribute("class",classname);

        if(id != null)
            element.setAttribute("id",id);

        if(innerText != null)
            element.innerHTML = innerText;
        
        return element;
    }

    static newElementNS(tagName, classname=null, id=null, width=null, height=null, viewBox=null){
        let element = document.createElementNS("http://www.w3.org/2000/svg", tagName);

        if(classname != null)
            element.setAttributeNS(null,"class",classname);
        
        if(id != null)
            element.setAttributeNS(null,"id",id);
        
        if(width != null)
            element.setAttributeNS(null,"width",width);
        
        if(height != null)
            element.setAttributeNS(null,"height",height);
        
        if(viewBox != null)
            element.setAttributeNS(null,"viewBox",viewBox);

        return element;
    }

}

class RadioParent{
    constructor(id){
        this.id = id;
        this.element = document.getElementById(id);
        this.guardarBtn = Dom.newElement("div","saveBtn",this.id+"-saveBtn","guardar");
        this.cancelarBtn = Dom.newElement("div","saveBtn",this.id+"-cancelBtn","cancelar");
        this.setTriggers(),
        this.setListeners();        
    }




    notify(data){
        let event = new CustomEvent(data.event,{"detail":data});
        this.element.dispatchEvent(event);
    }

    showSaveBtn(){
        document.getElementById("bindOptions").appendChild(this.guardarBtn);
    }

    removeSaveBtn(){
        document.getElementById("bindOptions").removeChild(this.guardarBtn);
    }

    lock(){
        this.element.onmouseenter = ()=>{};
        this.element.onmouseleave = ()=>{};
        this.radioActive = ()=>{};
    }

    unlock(){
        this.setTriggers();
    }

    setTriggers(){
        this.element.onmouseenter = () =>{
            myApp.sendNotification({
                "providerId": this.id,
                "event":"mainMode",
            });
        }

        this.element.onmouseleave = () =>{
            myApp.sendNotification({
                "providerId": this.id,

                "event":"supportMode",
            });
        }

/*+++*/ this.brotherRadioActive=(e)=>{
            myApp.sendNotification({
                "providerId": this.id,
                "event":"bindStart",
                "color":e.detail.color
            });
        }

/*+++*/ this.brotherRadioDone=()=>{
            myApp.sendNotification({
                "providerId": this.id,
                "event":"bindDone",
            });
        };

        this.radioActive = (e) => {  
            this.showSaveBtn();          
            myApp.sendNotification({
                "providerId": this.id,
                "event":"radioChange",
                "focusOn":e.detail.providerId,
                "color": e.detail.color
            });
            this.lock();
            myApp.sendNotification({
                "providerId": this.id,
                "event":"brotherActive",
            });
            myApp.sendNotification({
                "providerId": this.id,
                "event":"brotherActive",
            });
/*+++*/ myApp.sendNotification({
                "providerId": this.id,
                "event":"brotherRadioActive",
                "color":e.detail.color
            });
        };
        

        this.guardarBtn.onclick = ()=>{
            myApp.sendNotification({
                "providerId": this.id,
                "event":"radioDone",
            });
            this.removeSaveBtn();
            this.unlock();
            myApp.sendNotification({
                "providerId": this.id,
                "event":"brotherDone",
            });
            
/*+++*/     myApp.sendNotification({
                "providerId": this.id,
                "event":"brotherRadioDone",
            });

        }

        this.brotherActive = () => this.lock();
        this.brotherDone = () => this.unlock();
    }

    setListeners(){

        this.element.addEventListener("radioActive",this.radioActive,false);
        this.element.addEventListener("brotherActive",this.brotherActive,false);
        this.element.addEventListener("brotherDone",this.brotherDone,false);
        this.element.addEventListener("brotherRadioActive",this.brotherRadioActive,false);
        this.element.addEventListener("brotherRadioDone",this.brotherRadioDone,false);

    }

}

class App{
   
    constructor(requiredClasses){
        this.dom = new Dom();
        this.bindHtmlElements(requiredClasses);
    }

    bindHtmlElements(requiredClasses){
        
        for(let reqClass of requiredClasses){
            
            let htmlElements = document.getElementsByClassName(reqClass);
            
            if (htmlElements.length > 0) {
                
                for(let element of htmlElements){
                    
                    switch(reqClass){

                        case "ReticulaEl": this.dom.registerElement(new ReticulaEl(element.id));
                        break;

                        default: console.log(`Class "${reqClass}" not found or registrer on the builder`);
                    }
                }
            } else console.log(`no "${reqClass}" elements found`);

        }
    }

    registerElement(element){
        this.dom.registerElement(element);
    }

    registerProvider(providerId){
        this.dom.registerProvider(providerId);
    }

    registerSubscriber(providerId, subscriberId){
        this.dom.registerSubscriber(providerId, subscriberId);
    }

    findDomIndex(id){
        return this.dom.indexDirectory.get(id);
    }

    getSubscribers(providerId){
        return this.dom.notificationDirectory.get(providerId);
    }

    isSusribed(providerId, subscriberId){

        for(let sub of myApp.getSubscribers(providerId)){
            if(sub == subscriberId)
                return true;
        }

        return false;
    }

    sendNotification(data){
        let subscribers = this.getSubscribers(data.providerId);

        if(subscribers){   
            for(let subscriber of subscribers){
                this.dom.elements[this.findDomIndex(subscriber)].notify(data);
            }
        }

    }

    showDom(){
        this.dom.show();
    }
}

class ReticulaEl{

    constructor(id, buildCreatig=false, name=null, alias=null, color=null, parentId=null, state = false){

        //Set id independently of building mode
        this.id = id;
        this.alias = alias;
        this.providerColor = color;
        this.restingColor = color;
        this.currentProvider = {
            id: null,
            color: null
        };

        //State: active / inactive
        this.state = state;

        //Declare the edit and delete buttons
        this.editBtn = null;
        this.deleteBtn = null;

        //card is the main element of the component
        this.card = null;

        //ColorHeadBar
        this.cardHead = null;
        
        //cardActive is the group of elements to show when the component is active
        this.cardActive = null;

        this.radioParentId = null;

        //--------------------------------- Buildmode Logic ------------------------------------------------

        // (0) bulidMode defines if needs to create a new html element and append to the parent 
        this.buildMode = buildCreatig;
        
        // (1.1) if buildmode is creating, create a new card and set the name and color. Finally append tho the parent
        if(buildCreatig){
            this.card = Dom.newElement("div","ReticulaEl",this.id,name);
            this.card.setAttribute("data-color",color);
            this.radioParentId = parentId;
            document.getElementById(this.radioParentId).appendChild(this.card);
        }

        // (1.2) else just Bind an existing div
        else {this.card = document.getElementById(this.id); this.alias = this.card.dataset.alias;
        }

        // (2) finally proced to create, append and bind the rest of the inner elements
        this.build();

        // (3) Set listeners to hear the events and notifications
        this.setDefaultTriggers();
        this.setDefaultListeners();

        // (4) Change to default state
        this.changeState("supportResting");
    }

    //Building HTML content ..............................................................................

    build(){

        // (1) Set the NameAtribute taken by the Card and clean it to use it in the ActiveLabel
        if(this.card.innerHTML != ""){
            this.name = this.card.innerHTML;
            this.card.innerHTML = "";
        }

        // (2) Create a mask to hide the Active-Tag elements
        let cardMask = Dom.newElement("div","MatriculaElMask");

            // (3) Create a group of the elements to show when the stae is active
            this.cardActive = Dom.newElement("div","ReticulaEl-Active",`${this.id}-Active`);
            
            // (4) Set the color atribute to indicate when its active from dataset. Or set default css class property
            if(this.card.dataset.color != null){
                this.color = this.card.dataset.color;
                this.color = this.card.dataset.color;
                this.cardActive.style.backgroundColor = this.color;
            }
            else this.color = this.cardActive.style.backgroundColor;
            
                // (5) Create a group for delete btn
                let cardActiveDelete = Dom.newElement("div","ReticulaEl-Active-Delete");

                    // (6) Create the svg delete botton giving an id compose by the card id and the -DeleteBtn prefix and bind to the deleteBtn atribute
                    this.deleteBtn = Dom.newElementNS("svg","ReticulaEl-Active-DeleteBtn",`${this.id}-DeleteBtn`,"20","20","0 0 20 40");
                    
                    // (7) Create the cross parth icon
                    let deletePath = Dom.newElementNS("path");
                    deletePath.setAttributeNS(null,"d","M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z");

                    // (8) Append the path to the botton and append the botton to the activeDeleteGroup
                    this.deleteBtn.appendChild(deletePath);
                    cardActiveDelete.appendChild(this.deleteBtn);
                
                // (9) Create a label for the active state and write inner the html
                let cardActiveLabel = Dom.newElement("div","ReticulaEl-Active-Label",null,this.name);

                // (10) Create a group for the editBtn and set an id composite by the card id and the DeleteBtn postfix,
                //      The button is assigned to all the div because the edit svg icon is to small 
                this.editBtn = Dom.newElement("div","ReticulaEl-Active-EditBtn",`${this.id}-DeleteBtn`);
                    
                    // (11) create the edit svg elemente
                    let editSvg = Dom.newElementNS("svg",null,null,"20","20","0 0 25 25");

                    // (12) create the pencil path icon
                    let editPath = Dom.newElementNS("path");
                    editPath.setAttributeNS(null,"d","M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z");

                    // (13) Append the path to the botton and append the botton to the editBtnGroup
                    editSvg.appendChild(editPath);
                    this.editBtn.appendChild(editSvg);
            
            // (14) append the buttons an label tho the active group
            this.cardActive.appendChild(cardActiveDelete);
            this.cardActive.appendChild(cardActiveLabel);
            this.cardActive.appendChild(this.editBtn);

            // (15) create the head and label tho the inactive state
            this.cardHead = Dom.newElement("div","ReticulaEl-Head",`${this.id}-ReticulaEl-Head`);
            let cardLabel = Dom.newElement("div","ReticulaEl-Label",null,`${this.alias}`);        
        
        // (16) Append the elements to the mask and append the mask to the card
        cardMask.appendChild(this.cardActive);
        cardMask.appendChild(this.cardHead);
        cardMask.appendChild(cardLabel);
        this.card.appendChild(cardMask);

        //---------------------------------Btns behavor-------------------------------------------------
        this.deleteBtn.onclick = () => eliminar(this.id) //alert(`Seguro que deseas borrar la Matricula de ${this.name}?`);
        this.editBtn.onclick = () => editar(this.id)//var urlEditar = http://127.0.0.1:8000/carreras&especialidades/editarcarrera/${this.id};
            //setTimeout("location.href=`http://127.0.0.1:8000/carreras&especialidades/editarcarrera/${this.id}`", 1); //{
            //alert(urlEditar);
            //mostrarPanel();
        //}
    }

    
    //Drawing functions .................................................................................
    
    changeHeadBarColor(color = this.restingColor){
        this.cardHead.style.backgroundColor = color;
    }

    showActiveContent(show = true){
        if(show){
            this.cardActive.style.height = "100%"
            this.cardActive.style.transform = "translateY(0px)";
        } else{
            this.cardActive.style.height = "0px";
            this.cardActive.style.transform = "translateY(-110px)";
        }
    }

    changeActiveColor(color = this.color){
        this.cardActive.style.backgroundColor = color;
    }

    switchColors(reset=false){
        if(reset){
            this.changeActiveColor(this.color);
            this.changeHeadBarColor(this.restingColor);
        }
        else{
            this.changeActiveColor(this.currentProvider.color);
            this.changeHeadBarColor(this.currentProvider.color);
        }
    }


    //Data functions
    changeCurrentProvider(newProvider){
        this.currentProvider = newProvider;
    }

    lock(){
        this.setDefaultTriggers();
        this.onRadioDone = ()=> this.unlock();
    }

    unlock(){
        this.changeState("supportResting");
    }


    //Trigers, Listeners and data notification catchers ................................................

    setDefaultTriggers(){
        this.onMouseEnter = ()=>{};
        this.onMouseLeave = ()=>{};
        this.onClick = ()=>{};

        this.onProviderMouseEnter = ()=>{};
        this.onProviderMouseLeave = ()=>{};
        this.onProviderActive = ()=>{};
        this.onProviderResting = ()=>{};

        this.onRadioChange = ()=>{};
        this.onRadioDone = ()=>{};

        this.onBindStart = ()=>{};
        this.onBindDone = ()=>{};

        this.onSupportMode = ()=>{};
        this.onMainMode = ()=>{};
    }

    setDefaultListeners(){

        //User input listeners
        this.card.onmouseenter = ()=> this.onMouseEnter();
        this.card.onmouseleave = ()=> this.onMouseLeave();
        this.card.onclick = ()=> this.onClick();
        
        //Data notification catchers
        this.providerMouseEnter = (e) => this.onProviderMouseEnter(e.detail);
        this.providerMouseLeave = (e) => this.onProviderMouseLeave(e.detail);
        this.providerActive = (e) => this.onProviderActive(e.detail);
        this.providerResting = () => this.onProviderResting();

        this.radioChange = (e) => this.onRadioChange(e.detail);
        this.radioDone = () => this.onRadioDone();

        this.bindStart = (e) => this.onBindStart(e.detail);
        this.bindDone = () => this.onBindDone();
        
        this.supportMode = () => this.onSupportMode();
        this.mainMode = () => this.onMainMode();

        //Notidication listeners
        this.card.addEventListener("providerMouseEnter",this.providerMouseEnter,false);
        this.card.addEventListener("providerMouseLeave",this.providerMouseLeave,false);
        this.card.addEventListener("providerActive",this.providerActive,false);
        this.card.addEventListener("providerResting",this.providerResting,false);

        this.card.addEventListener("radioChange",this.radioChange,false);
        this.card.addEventListener("radioDone",this.radioDone,false);

        this.card.addEventListener("bindStart",this.bindStart,false);
        this.card.addEventListener("bindDone",this.bindDone,false);

        


        this.card.addEventListener("supportMode",this.supportMode,false);
        this.card.addEventListener("mainMode",this.mainMode,false);
    }


    //State behavor .....................................................................................
    changeState(targetState){

        this.setDefaultTriggers();

        switch(targetState){
            
            case "mainResting":{
                this.onMouseEnter = () =>{
                    this.showActiveContent();
                    myApp.sendNotification({
                        "providerId": this.id,
                        "event": "providerMouseEnter",
                        "color":this.color
                    }); 
                }
                this.onMouseLeave = () => {
                    this.showActiveContent(false);
                    myApp.sendNotification({
                        "providerId": this.id,
                        "event": "providerMouseLeave"
                    });
                }
                this.onClick = () => {
                    myApp.sendNotification({
                        "providerId": this.id,
                        "event":"radioActive",
                        "color":this.color
                    });
                    myApp.sendNotification({
                        "providerId": this.id,
                        "event":"providerActive",
                        "color":this.color
                    });
                    this.changeState("mainActive");
                }
                this.onRadioChange = (data)=> {this.lock()};
                this.onRadioDone = ()=> this.unlock();
                this.onSupportMode = ()=> this.changeState("supportResting");
            } break;
           
            case "mainActive":{
                this.onRadioDone = () =>{
                    this.showActiveContent(false);
                    myApp.sendNotification({
                        "providerId": this.id,
                        "event":"providerResting",
                    });
                    this.unlock();
                }

                this.onSupportMode = ()=> {this.showActiveContent(false); this.changeState("supportResting")};          
            } break;

            case "supportResting":{
 /*MMM*/        this.onMouseEnter = ()=> {this.switchColors(); this.showActiveContent();}
 /*MMM*/        this.onMouseLeave = ()=> {this.switchColors(true); this.showActiveContent(false);}
                this.onClick = ()=> this.changeState("supportActive"); // NOTIFY DATA!!!!
 /*MMM*/        this.onProviderMouseEnter = (data)=> {this.changeCurrentProvider({id:data.providerId, color:data.color}); this.switchColors();}
 /*MMM*/        this.onProviderMouseLeave = ()=> this.switchColors(true);
                this.onProviderActive = ()=> {this.showActiveContent(); this.changeState("supportActive")};
 /*+++*/        this.onBindStart = (data)=>{this.changeCurrentProvider({id:data.providerId, color:data.color});};
 /*+++*/        this.onBindDone = ()=> this.switchColors(true);
 /*MMM*/        this.onMainMode = () =>{this.switchColors(true); this.changeState("mainResting");};
            } break;

            case "supportActive":{
                this.onMouseEnter = ()=> this.showActiveContent(false);
                this.onMouseLeave = ()=> this.showActiveContent();
 /*MMM*/        this.onClick = ()=> {this.changeHeadBarColor(this.restingColor); this.changeState("supportResting");} //DATA NOTIFICATION!!!!
/*+++*/         this.onBindDone = ()=> {this.switchColors(true); this.showActiveContent(false); this.changeState("supportResting")};
/*MMM*/         this.onProviderResting = ()=> {this.showActiveContent(false); this.switchColors(true); this.changeState("supportResting")};
                // this.onBindModeResting = ()=> {this.showActiveContent(false); this.changeActiveColor(this.color); this.changeState("supportResting")};
            } break;

        }

        this.state = targetState;
    }


    
    //Main notification interface ........................................................................
    notify(data){
        let event = new CustomEvent(data.event,{"detail":data});
        this.card.dispatchEvent(event);
    }
}
function mostrarModal(){
    document.getElementById('modal-wrapper').style.display='block'
}
function cerrarModal(){
    //document.getElementById('modal-wrapper').style.display='none'
    setTimeout("location.href='http://127.0.0.1:8000/carreras&especialidades/'",1);
}
function cerrarModalAtributos(){
    //document.getElementById('modal-wrapper').style.display='none'
    setTimeout("location.href='http://127.0.0.1:8000/atributos/'",1);
}
function cerrarModalProfesores(){
    //document.getElementById('modal-wrapper').style.display='none'
    setTimeout("location.href='http://127.0.0.1:8000/profesores/'",1);
}
function cerrarModalAlumnos(){
    //document.getElementById('modal-wrapper').style.display='none'
    setTimeout("location.href='http://127.0.0.1:8000/alumnos/'",1);
}
function cerrarModalGrupos(){
    //document.getElementById('modal-wrapper').style.display='none'
    setTimeout("location.href='http://127.0.0.1:8000/grupos/'",1);
}
function editar(id){
    var str = id.split("-");
    var urlEditar = "location.href='http://127.0.0.1:8000/carreras&especialidades/editar";
    if(str[1] == "C")
        urlEditar+= "carrera/" + str[0] + "'"
    if(str[1] == "E")
        urlEditar+= "especialidad/" + str[0] + "'"
    setTimeout(urlEditar,1);
}

function eliminar(id){
    var str = id.split("-");
    var urlEliminar = "location.href='http://127.0.0.1:8000/carreras&especialidades/eliminar";
    if(str[1] == "C")
        urlEliminar+= "carrera/" + str[0] + "'"
    if(str[1] == "E")
        urlEliminar+= "especialidad/" + str[0] + "'"
    setTimeout(urlEliminar,1);
}
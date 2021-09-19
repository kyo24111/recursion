class Point{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }
}

class Line{
    constructor(startPoint, endPoint){
        this.startPoint = startPoint;
        this.endPoint = endPoint;
    }

    lineLength(){
        let lineSegment = Math.sqrt((this.startPoint.x - this.endPoint.x)**2 + (this.startPoint.y - this.endPoint.y)**2);

        return lineSegment;
    }

    vector(){
        return new Point(this.endPoint.x - this.startPoint.x, this.endPoint.y - this.startPoint.y);
    }
}

class QuadrilateralShape{
    constructor(lineAB, lineBC, lineCD, lineDA){
        this.lineAB = lineAB;
        this.lineBC = lineBC;
        this.lineCD = lineCD;
        this.lineDA = lineDA;
    }

    getShapeType(){
         // 四角形の名称を返します。square(正方形)、rectangle(長方形)、kite(凧)、rhombus(ひし形)、parallelogram(平行四辺形)、trapezoid(台形)、その他があります。
         // 判定条件
         //　　四角形かどうか.内角の和が360°ではない -> 四角形ではない.
         // 対角線が直交しているかどうか.　
         //　　直交している　-> 正方形、ひし形、凧　
         //　　直交していない -> 長方形、平行四辺形、台形、その他
         //     内積　＝　0　 -> 直交している
         //     内積　＝　|a||b| or -|a||b| -> 平行となっている
         
         //対角線のベクトルAC、ベクトルBD
        let vectorAC = new Point(this.lineAB.vector().x + this.lineBC.vector().x, this.lineAB.vector().y + this.lineBC.vector().y);
        let vectorBD = new Point(this.lineBC.vector().x + this.lineCD.vector().x, this.lineBC.vector().y + this.lineCD.vector().y);

        
        let innerProductAC_BD = this.getInnerProduct(vectorAC, vectorBD);  //ベクトルACとBDの内積.　
        let innerProductAB_CD = this.getInnerProduct(this.lineAB.vector(), this.lineCD.vector());  //ベクトルABとCDの内積.　
        let innerProductBC_DA = this.getInnerProduct(this.lineBC.vector(), this.lineDA.vector());  //ベクトルBCとDAの内積.　

        //四角形かどうかを判定する
        let sumOfInternalAngle = Math.round((this.getAngle("BAD") + this.getAngle("ABC") + this.getAngle("BCD") + this.getAngle("ADC"))/10)*10;
        if(sumOfInternalAngle !== 360){ return "NOT Quadrilateral Shape"};

        //四角形のタイプを判定する
        if(innerProductAC_BD === 0){
            // 正方形. 全ての角度が90°
            if(this.getAngle("BAD") === 90 && this.getAngle("ABC") === 90 && this.getAngle("BCD") === 90){ return "square"}; 
            //　　ひし形.　全てのへんの長さが同じ
            if(this.lineAB.lineLength() === this.lineBC.lineLength() && this.lineAB.lineLength() === this.lineCD.lineLength() && this.lineAB.lineLength() === this.lineDA.lineLength()){ return "rhombus"};
            //　　凧.　どちらかの対角が等しい
            if(this.getAngle("BAD") === this.getAngle("BCD") || this.getAngle("ABC") === this.getAngle("ADC")){　return "kite"};
            return "other";
        }else{
            // 長方形.　全ての角度が90°
            if(this.getAngle("BAD") === 90 && this.getAngle("ABC") === 90 && this.getAngle("BCD") === 90){ return "rectangle"}; 
            //　平行四辺形.　向かい合う2組の辺が平行
            if(Math.abs(innerProductAB_CD) === Math.floor(this.lineAB.lineLength() * this.lineCD.lineLength()) && Math.abs(innerProductBC_DA) === Math.floor(this.lineBC.lineLength()*this.lineDA.lineLength())){ return "parallelogram"};
            // 台形.　向かい合う2組の辺のうち、どちらかが平行
            if(Math.abs(innerProductAB_CD) === this.lineAB.lineLength()*this.lineCD.lineLength() || Math.abs(innerProductBC_DA) === this.lineBC.lineLength()*this.lineDA.lineLength()){ return "trapezoid"}
            return "other";
        }
    }

    getPerimeter(){
        // 四角形の周囲の長さを返します。
        return this.lineAB.lineLength() + this.lineBC.lineLength() + this.lineCD.lineLength() + this.lineDA.lineLength();
    }

    getArea(){
        // 四角形の面積を返します。shapeType別に計算方法を変更する
        // 四角形の面積は三角形BADと三角形BCDそれぞれの面積の和
        //　　面積S = (1/2) * |a||b| * sinθ

        let area1 = (1/2) * (this.lineAB.lineLength() * this.lineDA.lineLength()) * Math.sin(this.getAngle("BAD") * Math.PI / 180); //三角形BADの面積
        let area2 = (1/2) * (this.lineBC.lineLength() * this.lineCD.lineLength()) * Math.sin(this.getAngle("BCD") * Math.PI / 180); //三角形BCDの面積

        return area1 + area2;
    }

    getInnerProduct(vector1, vector2){
        //内積を返す.
        return vector1.x * vector2.x + vector1.y * vector2.y; 
    }

    getAngle(angleString){
        // BAD、ABC、BCD、ADCの角度を返します。
        //ベクトルの内積から角度を算出する

        let line1;
        let line2;

        if(angleString === "BAD"){
            line1 = this.lineDA;
            line2 = this.lineAB;
        }
        if(angleString === "ABC"){
            line1 = this.lineAB;
            line2 = this.lineBC;
        }
        if(angleString === "BCD"){
            line1 = this.lineBC;
            line2 = this.lineCD;
        }
        if(angleString === "ADC"){
            line1 = this.lineCD;
            line2 = this.lineDA;
        }
        
        //line1のベクトルは逆方向なので、-1を掛ける.
        let innerProduct = (-1) * this.getInnerProduct(line1.vector(), line2.vector()); // 内積. 
        let cos = innerProduct / (line2.lineLength() * line1.lineLength());　// cosθ
        
        return Math.round(Math.acos(cos) * 180 / Math.PI);
    }
    draw(){
        // ﹍﹉ | \ /を使って、四辺形をテキストとして描画します。1文字は平面上における距離です。|は直角、/は45度、\は135度の場合に用いられます。
        // 全ての角度が45°, 90°, 135°のいずれかの場合のみ描画する.　　つまり　少なくとも1　つの角が　　θ % 45 !== 0 の場合　描画しない.

        if(this.getAngle("BAD") % 45 !== 0 || this.getAngle("ABC") % 45 !== 0 || this.getAngle("BCD") % 45 !== 0 || this.getAngle("BCD") % 45 !== 0){return "四角形を描画できません";}

        let top;
        let mid;
        let bottom;
        let height;

        //正方形、長方形の描画
        if(this.getShapeType() === "square" || this.getShapeType() === "rectangle"){
            top = "|" +  "﹉".repeat(this.lineAB.lineLength()) + "|"
            mid = "|" +  "　".repeat(this.lineAB.lineLength()) + "|"
            bottom = "|" +  "﹍".repeat(this.lineAB.lineLength()) + "|"
            height = this.lineDA.lineLength() - 2;

            console.log(top);
            for(let i=0; i < height; i++){
                console.log(mid);
            }
            console.log(bottom);
        }

        //　平行四辺形の描画
        if(this.getShapeType() === "parallelogram"){
            //x軸と垂直な辺があるかどうかで平行四辺形のタイプを判別する.
            let innerProductX_AB = this.getInnerProduct(new Point(1, 0), this.lineAB.vector());
            let innerProductX_BC = this.getInnerProduct(new Point(1, 0), this.lineBC.vector());

            if(innerProductX_AB === 0 || innerProductX_BC === 0){
                console.log("　　/|");
                console.log("　/　|");
                console.log("/　 　|");
                console.log("|　 　|");
                console.log("|　 　/");
                console.log("|　 /　");
                console.log("|/　　");
            }else{
                console.log(" 　/﹉﹉﹉﹉/");
                console.log("  /　　　　 / ");
                console.log("/﹍﹍﹍﹍/  ");
            }
        }
        if(this.getShapeType() === "trapezoid"){
            console.log(" 　／﹉﹉＼　　");
            console.log("／﹍﹍﹍﹍﹍＼");
        }
        return "";

    }

    test(){
        console.log("---------------------")
        console.log("四角形の名称　： " + this.getShapeType());
        console.log("線分AB = " + Math.round(this.lineAB.lineLength() * 10)/10);
        console.log("線分BC = " + Math.round(this.lineBC.lineLength() * 10)/10);
        console.log("線分CD = " + Math.round(this.lineCD.lineLength() * 10)/10);
        console.log("線分DA = " + Math.round(this.lineDA.lineLength() * 10)/10);
        console.log("ベクトルAB = " + "(" + this.lineAB.vector().x + ", " + this.lineAB.vector().y + ")");
        console.log("ベクトルBC = " + "(" + this.lineBC.vector().x + ", " + this.lineBC.vector().y + ")");
        console.log("ベクトルCD = " + "(" + this.lineCD.vector().x + ", " + this.lineCD.vector().y + ")");
        console.log("ベクトルDA = " + "(" + this.lineDA.vector().x + ", " + this.lineDA.vector().y + ")");
        console.log("∠BAD = " + this.getAngle("BAD") + "°");
        console.log("∠ABC = " + this.getAngle("ABC") + "°");
        console.log("∠BCD = " + this.getAngle("BCD") + "°");
        console.log("∠ADC = " + this.getAngle("ADC") + "°");
        console.log("面積S = " + Math.round(this.getArea() * 10)/10);
        console.log("---------------------")
    }
}


//------------------------------------------------------------------------------
// TEST CASE

// square（正方形）
const lineAB1 = new Line(new Point(0, 0), new Point(5, 0));
const lineBC1 = new Line(new Point(5, 0), new Point(5, 5));
const lineCD1 = new Line(new Point(5, 5), new Point(0, 5));
const lineDA1 = new Line(new Point(0, 5), new Point(0, 0));
const square = new QuadrilateralShape(lineAB1, lineBC1, lineCD1, lineDA1);
// square.test();
// square.draw();

// rectangle（長方形）
const lineAB2 = new Line(new Point(0, 0), new Point(8, 0));
const lineBC2 = new Line(new Point(8, 0), new Point(8, 5));
const lineCD2 = new Line(new Point(8, 5), new Point(0, 5));
const lineDA2 = new Line(new Point(0, 5), new Point(0, 0));
const rectangle = new QuadrilateralShape(lineAB2, lineBC2, lineCD2, lineDA2);
// rectangle.test();
// rectangle.draw();

// parallelogram1(平行四辺形)
const lineAB3 = new Line(new Point(0, 0), new Point(2, 2));
const lineBC3 = new Line(new Point(2, 2), new Point(2, 6));
const lineCD3 = new Line(new Point(2, 6), new Point(0, 4));
const lineDA3 = new Line(new Point(0, 4), new Point(0, 0));
const parallelogram1 = new QuadrilateralShape(lineAB3, lineBC3, lineCD3, lineDA3);
// parallelogram1.test();
// parallelogram1.draw();

// parallelogram2(平行四辺形)
const lineAB4 = new Line(new Point(0, 0), new Point(4, 0));
const lineBC4 = new Line(new Point(4, 0), new Point(6, 2));
const lineCD4 = new Line(new Point(6, 2), new Point(2, 2));
const lineDA4 = new Line(new Point(2, 2), new Point(0, 0));
const parallelogram2 = new QuadrilateralShape(lineAB4, lineBC4, lineCD4, lineDA4);
// parallelogram2.test();
// parallelogram2.draw();

// trapezoid(台形)
const lineAB5 = new Line(new Point(0, 0), new Point(6, 0));
const lineBC5 = new Line(new Point(6, 0), new Point(4, 2));
const lineCD5 = new Line(new Point(4, 2), new Point(2, 2));
const lineDA5 = new Line(new Point(2, 2), new Point(0, 0));
const trapezoid = new QuadrilateralShape(lineAB5, lineBC5, lineCD5, lineDA5);
// trapezoid.test();
// trapezoid.draw();


// rhombus(ひし形)
const lineAB6 = new Line(new Point(1, 1), new Point(3, 0));
const lineBC6 = new Line(new Point(3, 0), new Point(5, 1));
const lineCD6 = new Line(new Point(5, 1), new Point(3, 2));
const lineDA6 = new Line(new Point(3, 2), new Point(1, 1));
const rhombus = new QuadrilateralShape(lineAB6, lineBC6, lineCD6, lineDA6);
// rhombus.test();

// kite(凧)
const lineAB7 = new Line(new Point(1, 1), new Point(3, 0));
const lineBC7 = new Line(new Point(3, 0), new Point(10, 1));
const lineCD7 = new Line(new Point(10, 1), new Point(3, 2));
const lineDA7 = new Line(new Point(3, 2), new Point(1, 1));
const kite = new QuadrilateralShape(lineAB7, lineBC7, lineCD7, lineDA7);
// kite.test();

// other(その他)
const lineAB8 = new Line(new Point(1, 1), new Point(4, -2));
const lineBC8 = new Line(new Point(4, -2), new Point(10, 3));
const lineCD8 = new Line(new Point(10, 3), new Point(5, 6));
const lineDA8 = new Line(new Point(5, 6), new Point(1, 1));
const other = new QuadrilateralShape(lineAB8, lineBC8, lineCD8, lineDA8);
// other.test();

// NOT(四角形ではない)
const lineAB9 = new Line(new Point(1, 1), new Point(5, 6));
const lineBC9 = new Line(new Point(5, 6), new Point(10, 1));
const lineCD9 = new Line(new Point(10, 1), new Point(3, 2));
const lineDA9 = new Line(new Point(3, 2), new Point(1, 1));
const notQuadrilateral = new QuadrilateralShape(lineAB9, lineBC9, lineCD9, lineDA9);
// notQuadrilateral.test();

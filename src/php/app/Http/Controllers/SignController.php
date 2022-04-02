<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class SignController extends Controller
{
    public function signinPage(Request $request){
        $email = $request->session()->get('email', '');
        $isLogin = $request->session()->get('isLogin', false);
        $params = ['email'=> $email, 'isLogin'=>$isLogin];
        return view('sign/signin', $params);
    }

    public function signin(Request $request){
        $email = $request->email;
        $password = $request->email;
        $request->session()->put('email', $email);
        $request->session()->put('isLogin', true);
        return redirect('/');
    }

    public function signout(Request $request){
        $request->session()->forget('email');
        $request->session()->forget('isLogin');
        return redirect('/');
    }
}

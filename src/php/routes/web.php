<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\SignController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', [SignController::class, 'signinPage']);
Route::post('/', [SignController::class, 'signin']);
Route::post('/signout', [SignController::class, 'signout']);
